import os
import shutil
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

def get_image_taken_date(image_path):
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return None
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "DateTimeOriginal":
                # Format: "YYYY:MM:DD HH:MM:SS"
                return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except Exception as e:
        print(f"Error reading EXIF from {image_path}: {e}")
    return None

def move_files_after_date(img_folder, label_folder, dest_folder, date_str):
    input_date = datetime.strptime(date_str, "%d-%m-%Y")

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    img_files = [f for f in os.listdir(img_folder) if os.path.isfile(os.path.join(img_folder, f))]

    moved_files_count = 0

    for img_file in img_files:
        img_path = os.path.join(img_folder, img_file)

        taken_date = get_image_taken_date(img_path)

        if taken_date is None:
            print(f"No EXIF taken date found for {img_file}, skipping...")
            continue

        if taken_date > input_date:
            shutil.move(img_path, os.path.join(dest_folder, img_file))

            label_file = os.path.splitext(img_file)[0] + '.txt'
            label_path = os.path.join(label_folder, label_file)

            if os.path.exists(label_path):
                shutil.move(label_path, os.path.join(dest_folder, label_file))
            else:
                print(f"Warning: Label file not found for {img_file}")

            moved_files_count += 1

    print(f"Total files moved: {moved_files_count}")

if __name__ == "__main__":
    img_folder = input("Enter path to image folder: ").strip()
    label_folder = input("Enter path to label folder: ").strip()
    dest_folder = input("Enter path to destination folder: ").strip()

    date_input = input("Enter date (dd-mm-yyyy): ").strip()

    try:
        move_files_after_date(img_folder, label_folder, dest_folder, date_input)
    except Exception as e:
        print(f"Error: {e}")

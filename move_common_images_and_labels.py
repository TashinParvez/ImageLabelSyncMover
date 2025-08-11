import os
import shutil

def move_common_images_and_labels(pic_folder1, label_folder, pic_folder2, dest_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # List all images in pic_folder2 for quick lookup (set for speed)
    pic2_images = set(os.listdir(pic_folder2))

    moved_count = 0

    # Iterate over images in pic_folder1
    for img_file in os.listdir(pic_folder1):
        img_path1 = os.path.join(pic_folder1, img_file)

        # Only files, skip directories
        if not os.path.isfile(img_path1):
            continue

        # Check if same filename exists in pic_folder2
        if img_file in pic2_images:
            # Move image from pic_folder1 to destination
            shutil.move(img_path1, os.path.join(dest_folder, img_file))

            # Move corresponding label (.txt) from label_folder if exists
            label_file = os.path.splitext(img_file)[0] + '.txt'
            label_path = os.path.join(label_folder, label_file)

            if os.path.exists(label_path):
                shutil.move(label_path, os.path.join(dest_folder, label_file))
            else:
                print(f"Warning: Label file missing for {img_file}")

            moved_count += 1

    print(f"Total images (and labels) moved: {moved_count}")

if __name__ == "__main__":
    pic_folder1 = input("Enter path to pic folder 1: ").strip()
    label_folder = input("Enter path to label folder: ").strip()
    pic_folder2 = input("Enter path to pic folder 2: ").strip()
    dest_folder = input("Enter path to new destination folder: ").strip()

    try:
        move_common_images_and_labels(pic_folder1, label_folder, pic_folder2, dest_folder)
    except Exception as e:
        print(f"Error: {e}")

# ImageLabelSyncMover

**ImageLabelSyncMover** is a Python utility repository designed to simplify the management of image files and their corresponding label files (in `.txt` format). It contains two key scripts to automate common tasks involving image datasets:

1. **Date-based Image & Label Mover**
   Move images and their label files based on the photo’s original taken date (from EXIF metadata). Given a cutoff date, this script shifts all images taken *after* that date along with their labels to a specified folder.

2. **Matching Filename Image & Label Sync Mover**
   Compare two image folders and move images from the first folder — along with their label files — only if the same image filename exists in the second folder. This helps synchronize datasets based on image name overlaps.

---

### Use Cases

* Dataset cleaning and preparation for machine learning or computer vision tasks.
* Organizing image-label pairs for training or testing splits by date or file matching.
* Automating file organization workflows for large collections of images and annotations.

---

### Features

* Reads image EXIF metadata to accurately determine photo taken date.
* Moves files safely with warnings for missing labels.
* Simple command-line input for folder paths and date.
* Easily extendable for other filtering or sync conditions.

---

### Requirements

* Python 3.x
* Pillow (`pip install Pillow`) for EXIF date extraction.

# file_organizer.py
# Task 3 – File Automation: Organize files by type

from pathlib import Path
import shutil

# ====== SETTINGS ======
# Change this path to your test folder
SOURCE_DIR = Path(r"C:\Users\hasna\Desktop\test_folder")

# Preview mode (True = just show, False = really move)
DRY_RUN = False

# File type categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Video": [".mp4", ".avi", ".mkv"],
    "Code": [".py", ".ipynb", ".cpp", ".c", ".java"]
}

def get_category(ext):
    """Return category folder name based on file extension."""
    for category, extensions in CATEGORIES.items():
        if ext.lower() in extensions:
            return category
    return "Others"

# ====== MAIN PROGRAM ======
print("Organizing folder:", SOURCE_DIR)

for item in SOURCE_DIR.iterdir():
    if item.is_file():
        ext = item.suffix
        category = get_category(ext)
        target_folder = SOURCE_DIR / category
        target_folder.mkdir(exist_ok=True)

        new_path = target_folder / item.name
        if DRY_RUN:
            print("[PREVIEW]", item.name, "-->", new_path)
        else:
            shutil.move(str(item), str(new_path))
            print("[MOVED]", item.name, "-->", new_path)

import os
import shutil

# CHANGE THIS if your Downloads folder is elsewhere
DOWNLOADS_DIR = os.path.join(os.path.expanduser("~"), "Downloads")

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi"],
}

def organize_downloads():
    for file_name in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, file_name)

        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file_name)
        ext = ext.lower()

        moved = False
        for folder, extensions in FILE_TYPES.items():
            if ext in extensions:
                target_dir = os.path.join(DOWNLOADS_DIR, folder)
                os.makedirs(target_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(target_dir, file_name))
                moved = True
                break

        if not moved:
            other_dir = os.path.join(DOWNLOADS_DIR, "Others")
            os.makedirs(other_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(other_dir, file_name))

if __name__ == "__main__":
    organize_downloads()

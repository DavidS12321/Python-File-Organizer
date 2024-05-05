import os
import shutil

def create_dest_directories(dest_directories):
    """Create destination directories if they don't exist."""
    for dest_dir in dest_directories.values():
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

def move_files(src_path, dest_directories):
    """Move files to their respective destination directories."""
    for file in os.listdir(src_path):
        src_file_path = os.path.join(src_path, file)
        if os.path.isfile(src_file_path):
            file_extension = os.path.splitext(file)[-1].lower()
            dest_dir = dest_directories.get(file_extension)
            if dest_dir:
                dest_file_path = os.path.join(dest_dir, file)
                if not os.path.exists(dest_file_path):
                    shutil.move(src_file_path, dest_file_path)
                    print(f"{file} successfully moved to {dest_dir}")

def main():
    src_path = r"C:/Users/dshah/Downloads/"
    dest_directories = {
        ".pdf": "PDFs",
        ".jpg": "Images",
        ".png": "Images",
        ".txt": "Text files",
        ".zip": "Zip files",
        ".exe": "Application files",
        ".msi": "Application files",
        ".cs": "Unity downloads",
        ".unitypackage": "Unity downloads",
        ".mp3": "Audio Files",
        ".m4a": "Audio Files",
        ".mp4": "Video Files",
        ".mov": "Video Files",
        ".java": "Coding Files",
        ".py": "Coding Files",
        ".docx": "Documents",
        ".jar": "Jar Files",
        ".psd": "Other file types",
        ".json": "Other file types",
        ".dll": "Other file types"
    }
    # Append source path to destination directories
    dest_directories = {ext: os.path.join(src_path, dest) for ext, dest in dest_directories.items()}

    create_dest_directories(dest_directories)
    move_files(src_path, dest_directories)

if __name__ == "__main__":
    main()
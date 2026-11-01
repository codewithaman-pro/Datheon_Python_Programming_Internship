import os
import shutil
from pathlib import Path

# Official Extension Mapping for Automated Directory Sorting
EXTENSION_MAPPING = {
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.mp4': 'Videos',
    '.mkv': 'Videos',
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.py': 'Code',
    '.js': 'Code',
    '.html': 'Code'
}

def organize_directory(target_directory):
    """
    Automates filesystem operations and directory sorting using Python os/shutil libraries 
    based on official documentation standards.
    """
    path = Path(target_directory)
    
    if not path.exists():
        print(f"Error: The directory '{target_directory}' does not exist.")
        return

    moved_files_count = 0

    print(f"Starting organization for directory: {path.resolve()}")
    print("-" * 50)

    # Scanning directory using os.scandir() as per efficient file handling standards
    with os.scandir(path) as entries:
        for entry in entries:
            # Process files only, skipping directories
            if entry.is_file():
                file_path = Path(entry.path)
                file_extension = file_path.suffix.lower()

                # Check if the file extension matches our defined mapping dictionary
                if file_extension in EXTENSION_MAPPING:
                    category = EXTENSION_MAPPING[file_extension]
                    category_folder = path / category

                    # Dynamically create category subfolders if they do not exist
                    category_folder.mkdir(exist_ok=True)

                    destination_path = category_folder / file_path.name

                    try:
                        # Safely handle naming collisions and existing files
                        if destination_path.exists():
                            print(f"Skipped (Already exists): {file_path.name}")
                            continue

                        # Utilizing shutil.move for reliable file relocation
                        shutil.move(str(file_path), str(destination_path))
                        print(f"Moved: {file_path.name} ---> {category}/")
                        moved_files_count += 1

                    except PermissionError:
                        print(f"Permission denied: Unable to move {file_path.name}")
                    except Exception as e:
                        print(f"Error processing {file_path.name}: {e}")

    print("-" * 50)
    print(f"Organization Complete! Total files successfully relocated: {moved_files_count}")

if __name__ == "__main__":
    # Prompting user for target path or defaulting to current working directory
    target_dir = input("Enter the path of the directory you want to organize (Press Enter for current folder): ").strip()
    if not target_dir:
        target_dir = "."  # Current directory default
    organize_directory(target_dir)
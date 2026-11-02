
import os
import shutil
from pathlib import Path
from datetime import datetime

# Project paths
project_folder = Path(__file__).resolve().parent
source_folder = project_folder / "Test Files"
log_file = project_folder / "Organization Log.txt"

# Supported file categories
categories = {
    ".pdf": "Documents",
    ".txt": "Documents",
    ".docx": "Documents",
    ".csv": "Documents",
    ".xlsx": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".py": "Code",
    ".html": "Code",
    ".js": "Code"
}


def find_available_name(destination):
    """Find a filename that will not replace an existing file."""
    if not destination.exists():
        return destination

    number = 1

    while True:
        new_name = (
            f"{destination.stem} ({number}){destination.suffix}"
        )
        candidate = destination.with_name(new_name)

        if not candidate.exists():
            return candidate

        number += 1


def organize_files():
    if not source_folder.is_dir():
        print("Test Files folder does not exist.")
        return

    moved = 0
    failed = 0

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages = [f"\nFile Organization - {timestamp}"]

    print("\nAUTOMATED FILE ORGANIZER")
    print("Source:", source_folder)
    print("-" * 50)

    try:
        with os.scandir(source_folder) as entries:
            for entry in entries:
                try:
                    # Ignore folders and symbolic links
                    if not entry.is_file(follow_symlinks=False):
                        continue

                    source = Path(entry.path)
                    extension = source.suffix.lower()

                    category = categories.get(
                        extension, "Other"
                    )

                    destination_folder = source_folder / category
                    destination_folder.mkdir(exist_ok=True)

                    destination = destination_folder / source.name
                    destination = find_available_name(destination)

                    shutil.move(str(source), str(destination))

                    message = (
                        f"Moved: {source.name} -> "
                        f"{category}/{destination.name}"
                    )

                    print(message)
                    messages.append(message)
                    moved += 1

                except (OSError, shutil.Error) as error:
                    message = f"Failed: {entry.name} - {error}"
                    print(message)
                    messages.append(message)
                    failed += 1

    except OSError as error:
        message = f"Folder access error: {error}"
        print(message)
        messages.append(message)
        failed += 1

    summary = f"Files moved: {moved} | Failed: {failed}"

    print("-" * 50)
    print(summary)
    messages.append(summary)

    # Save the execution log
    try:
        with log_file.open("a", encoding="utf-8") as file:
            file.write("\n".join(messages) + "\n")

        print("Log saved:", log_file)

    except OSError as error:
        print("Could not save log:", error)


if __name__ == "__main__":
    organize_files()

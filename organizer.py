from email import errors
from pathlib import Path
from config import FILE_CATEGORIES
from shutil import move
import logging


def organize_files(folder, preview=False):

    files_scanned = 0
    files_moved = 0
    duplicates_renamed = 0
    errors = 0

    if preview:
        logging.info("Preview mode enabled.")

    for file in folder.iterdir():

        if file.is_file():

            files_scanned += 1

            print(file.suffix, file.name)

            # Find the category
            file_category = None

            for category, extensions in FILE_CATEGORIES.items():

                if file.suffix.lower() in extensions:
                    file_category = category
                    break

            else:
                file_category = "Others"

            # Create destination path
            destination_folder = folder / file_category
            destination_file = destination_folder / file.name

            # Preview mode
            if preview:
                if destination_file.exists():
                    print(f"[PREVIEW] {file.name} → {destination_folder} (will overwrite)")
                else:
                    print(f"[PREVIEW] {file.name} → {destination_folder}")

            # Normal organization mode
            else:

                destination_folder.mkdir(exist_ok=True)

                # Normal file
                if not destination_file.exists():

                    try:
                        move(file, destination_file)

                        logging.info(
                            f"{file.name} moved to {destination_folder}"
                        )
                        files_moved += 1

                    except Exception as e:

                        logging.error(
                            f"Error occurred while moving "
                            f"{file.name}: {e}"
                        )

                # Duplicate file
                else:

                    count = 1

                    new_name = (
                        f"{file.stem}_{count}{file.suffix}"
                    )

                    while (destination_folder / new_name).exists():

                        count += 1

                        new_name = (
                            f"{file.stem}_{count}{file.suffix}"
                        )

                    new_destination_file = (
                        destination_folder / new_name
                    )

                    try:

                        move(file, new_destination_file)

                        logging.info(
                            f"{file.name} renamed and moved to "
                            f"{new_destination_file}"
                        )
                        duplicates_renamed += 1 
                    except Exception as e:
                        errors += 1

                        logging.error(
                            f"Error occurred while moving "
                            f"{file.name}: {e}"
                        )
    print("\n========== ORGANIZATION SUMMARY ==========")
    print(f"Files scanned       : {files_scanned}")
    print(f"Files moved         : {files_moved}")
    print(f"Duplicates renamed  : {duplicates_renamed}")
    print(f"Errors              : {errors}")
    print("==========================================")
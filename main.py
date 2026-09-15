from pathlib import Path
import logging
from organizer import organize_files

# Create logs folder
log_folder = Path("logs")
log_folder.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Show logs in terminal
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logging.getLogger().addHandler(console_handler)

# Ask user for folder
folder_path = input("Enter the folder path to organize: ")
folder = Path(folder_path)

# Ask for mode
mode = input("Enter mode (preview/organize): ").lower()

# Validate folder
if not folder.exists() or not folder.is_dir():
    print("Invalid folder path.")

else:
    if mode == "preview":
        organize_files(folder, preview=True)

    elif mode == "organize":

        organize_files(folder, preview=False)

        logging.info("File organization completed.")

    else:

        print("Invalid mode. Please enter preview or organize.")
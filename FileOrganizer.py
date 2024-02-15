import os
import shutil

def organize_files(directory):
    # Dictionary to map file types to their respective folders
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Others': []  # Default folder for other file types
    }

    # Create folders if not exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Scan the directory and organize files
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            # Get the file extension
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension.lower()

            # Find the category for the file
            category = 'Others'
            for key, extensions in file_types.items():
                if file_extension in extensions:
                    category = key
                    break

            # Move the file to the corresponding folder
            destination_folder = os.path.join(directory, category)
            shutil.move(file_path, os.path.join(destination_folder, filename))
            print(f"Moved {filename} to {category} folder.")

if __name__ == "__main__":
    # Specify the directory to organize
    target_directory = input("Enter the directory path to organize: ")

    # Validate the directory
    if os.path.exists(target_directory):
        organize_files(target_directory)
        print("File organization complete.")
    else:
        print("Invalid directory path. Please provide a valid directory.")

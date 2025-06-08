import os

# Define the directory containing the files relative to the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script

# Path to the "data" folder
data_path = os.path.join(current_dir, "data")  # Path to the "data" folder

# Function to rename specific files in a specified folder and its subfolders
def rename_files_in_folder(folder_path):
    # Iterate through all the files in the directory and subdirectories
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Check if the current item is a file named "__data" with no extension
            if os.path.isfile(file_path) and filename == "__data" and not os.path.splitext(filename)[1]:
                # New file name with .bundle extension
                new_file_name = filename + ".bundle"
                new_file_path = os.path.join(root, new_file_name)

                # Rename the file
                os.rename(file_path, new_file_path)
                print(f"Renamed {filename} to {new_file_name}")

# Rename files in the data folder and its subfolders
rename_files_in_folder(data_path)

print("Renaming process completed.")
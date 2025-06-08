import os

# Define the path to the data folder
current_dir = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(current_dir, "data")

# Iterate through all files in the data folder and its subfolders
for root, dirs, files in os.walk(data_folder):
    for filename in files:
        file_path = os.path.join(root, filename)
        
        # Check if the file is indeed a .bundle file
        if os.path.isfile(file_path) and filename.endswith('.bundle'):
            # Construct the new filename without the .bundle extension
            new_filename = filename[:-7]  # Remove the last 7 characters ('.bundle')
            new_file_path = os.path.join(root, new_filename)

            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}' in {root}")
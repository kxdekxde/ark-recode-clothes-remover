import os
import UnityPy

UnityPy.config.FALLBACK_UNITY_VERSION = '2022.3.22f1'

# Paths for various folders
current_dir = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(current_dir, "data")

# Iterate through the "data" folder and its subfolders
for root, dirs, files in os.walk(data_folder):
    for file_name in files:
        if file_name.endswith(".bundle"):  # Targeting any .bundle files
            data_file_path = os.path.join(root, file_name)
            print(f"Decompressing {data_file_path}")

            try:
                # Load the Unity bundle
                env = UnityPy.load(data_file_path)

                # Save the bundle (this will be decompressed if it was compressed)
                with open(data_file_path, "wb") as f:
                    f.write(env.file.save())

                print(f"Saved decompressed {data_file_path}")

            except Exception as e:
                print(f"Error processing {file_name}: {str(e)}")

print("Decompression completed.")

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
            print(f"Compressing {data_file_path}")

            try:
                # Load the Unity bundle
                env = UnityPy.load(data_file_path)

                # Create a temporary file path for the compressed version
                temp_file_path = data_file_path + ".temp"
                
                # Save the bundle with LZ4 compression to a temporary file
                with open(temp_file_path, "wb") as f:
                    bundle_data = env.file.save(packer="lz4")
                    f.write(bundle_data)

                # Replace the original file with the compressed version
                os.remove(data_file_path)
                os.rename(temp_file_path, data_file_path)

                print(f"Successfully compressed {data_file_path}")

            except Exception as e:
                print(f"Error processing {file_name}: {str(e)}")
                # Clean up temp file if it exists
                if 'temp_file_path' in locals() and os.path.exists(temp_file_path):
                    os.remove(temp_file_path)

print("Compression completed.")
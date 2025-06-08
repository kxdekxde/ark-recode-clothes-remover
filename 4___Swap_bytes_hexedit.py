import os

# Define paths
current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the current script
data_folder = os.path.join(current_dir, "data")           # Main folder to process

# Define the byte patterns to search and replace
search_bytes = bytes.fromhex("04 4c 56 31 06 4c 56 31 5f 4d 04 4c 56 32 06 4c 56 32 5f 4d 04 4c 56 33 06 4c 56 33 5f 4d")
replace_bytes = bytes.fromhex("04 4c 56 33 06 4c 56 33 5f 4d 04 4c 56 32 06 4c 56 32 5f 4d 04 4c 56 31 06 4c 56 31 5f 4d")

def find_bundle_files(dir_path):
    """Find all .bundle files in directory and subdirectories"""
    bundle_files = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".bundle"):
                bundle_files.append(os.path.join(root, file))
    return bundle_files

# Find and process all .bundle files
bundle_files = find_bundle_files(data_folder)
processed_count = 0
total_replacements = 0

for bundle_path in bundle_files:
    print(f"Processing: {bundle_path}")
    replacements = 0
    
    try:
        # Read file as binary
        with open(bundle_path, "rb") as file:
            data = bytearray(file.read())
        
        # Find and replace all occurrences
        offset = 0
        while True:
            index = data.find(search_bytes, offset)
            if index == -1:
                break
                
            # Perform replacement
            data[index:index+len(search_bytes)] = replace_bytes
            print(f"  -> Modified at position {index}")
            replacements += 1
            total_replacements += 1
            offset = index + len(search_bytes)  # Move past this match
        
        # Only write back if we made changes
        if replacements > 0:
            with open(bundle_path, "wb") as file:
                file.write(data)
            processed_count += 1
            print(f"  -> Made {replacements} replacement(s) in this file")
        else:
            print("  -> Pattern not found in this file")
    
    except Exception as e:
        print(f"  !! Error processing file: {str(e)}")

print(f"\nProcessing complete. Modified {processed_count} of {len(bundle_files)} files.")
print(f"Total replacements made: {total_replacements}")
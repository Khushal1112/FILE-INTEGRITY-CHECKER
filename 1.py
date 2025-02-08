import os
import hashlib
import time
import json

def calculate_file_hash(file_path, hash_algorithm="sha256"):
    """Calculate the hash of a file."""
    hash_func = getattr(hashlib, hash_algorithm)()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except (FileNotFoundError, PermissionError):
        return None

def monitor_files(file_paths, hash_algorithm="sha256", interval=10):
    """Monitor files for changes by comparing their hash values."""
    hash_store = {}

    # Load previously saved hashes if available
    if os.path.exists("hash_store.json"):
        with open("hash_store.json", "r") as f:
            hash_store = json.load(f)

    try:
        while True:
            for file_path in file_paths:
                if not os.path.exists(file_path):
                    print(f"File not found: {file_path}")
                    continue

                current_hash = calculate_file_hash(file_path, hash_algorithm)
                if file_path in hash_store:
                    if hash_store[file_path] != current_hash:
                        print(f"[CHANGED] {file_path}")
                else:
                    print(f"[NEW FILE] {file_path}")

                # Update the hash store
                hash_store[file_path] = current_hash

            # Save the updated hashes to a file
            with open("hash_store.json", "w") as f:
                json.dump(hash_store, f, indent=4)

            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    # Files to monitor
    files_to_monitor = [
        "/home/khushal/Desktop/file.txt",
    ]
    
    # Ensure the files exist
    for file in files_to_monitor:
        if not os.path.exists(file):
            with open(file, "w") as f:
                f.write("Initial content.\n")

    # Start monitoring
    print("Monitoring files for changes. Press Ctrl+C to stop.")
    monitor_files(files_to_monitor, hash_algorithm="sha256", interval=5)


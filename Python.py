import os
import random

def increase_file_size(file_path, size_in_bytes):
    with open(file_path, "ab") as f:  # Open in append-binary mode
        # Generate random data to append
        random_data = os.urandom(size_in_bytes)
        f.write(random_data)

    print(f"File size increased by {size_in_bytes} bytes.")

# Usage
file_path = "your_file.txt"  # Path to the file you want to make bigger
size_in_bytes = 1000000  # Number of bytes to add (1MB in this example)

increase_file_size(file_path, size_in_bytes)

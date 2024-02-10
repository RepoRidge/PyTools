import numpy as np
import os
import re
from colorama import init, Fore, Style
import time

# Initialize colorama for ANSI color support in the terminal
init(autoreset=True)

def create_dat_file(filename, size_mb):
    # Calculate the number of bytes needed to achieve the desired size in MB
    size_bytes = size_mb * 1024 * 1024
    bytes_written = 0
    chunk_size = 1024 * 1024  # 1 MB chunk size

    print("Creating file...")

    with open(filename, 'wb') as f:
        while bytes_written < size_bytes:
            remaining_bytes = size_bytes - bytes_written
            bytes_to_write = min(chunk_size, remaining_bytes)

            # Generate random data of unsigned integer type at 8 bits (0-255)
            data = np.random.randint(0, 256, size=bytes_to_write, dtype=np.uint8)

            f.write(data)
            bytes_written += bytes_to_write

            # Calculate and print progress
            progress_percent = min(100.0, (bytes_written / size_bytes) * 100)
            print(f"Progress: {progress_percent:.2f}%  ({bytes_written / 1024 / 1024:.2f} MB / {size_mb} MB)", end='\r')

    print("\nFile creation completed.")
    return True

def is_valid_filename(filename):
    # Check if the filename contains only valid characters for Windows
    return not re.search(r'[<>:"/\\|?*]', filename)

if __name__ == "__main__":
    while True:
        try:
            desired_size = int(input(Fore.MAGENTA + "Enter the desired size of the file in MB: "))
            break
        except ValueError:
            print(Fore.RED + "Invalid input. You must enter an integer.")

    while True:
        filename = input(Fore.MAGENTA + "Enter the file name (without extension): ") + ".dat"
        if is_valid_filename(filename):
            break
        else:
            print(Fore.RED + "Special characters are not allowed in the filename.")

    success = create_dat_file(filename, desired_size)

    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    if success:
        print(Fore.GREEN + "File created successfully.")
        time.sleep(5)  # Wait 5 seconds before closing the terminal

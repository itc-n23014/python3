import os

def find_large_files(folder, size_threshold_mb):
    threshold = size_threshold_mb * 1024 * 1024
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            try:
                if os.path.getsize(path) > threshold:
                    print(f'{path} - {os.path.getsize(path) / (1024 * 1024):.2f} MB')
            except (FileNotFoundError, PermissionError):
                pass

source_directory = '/home/vagrant'
size_threshold_mb = 2

find_large_files(source_directory, size_threshold_mb)

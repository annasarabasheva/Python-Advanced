import os

path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, "my_first_file.txt")
try:
    os.remove(file_path)
    print("File deleted")
except FileNotFoundError:
    print('File already deleted!')


import os

path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, "my_first_file.txt")

with open(file_path, "w") as file:
    file.write("I just created my first file!")
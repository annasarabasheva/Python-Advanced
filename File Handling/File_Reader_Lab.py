import os

path_to_root = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(path_to_root, "numbers.txt")

with open(file_path, "r") as file:
    list_numbers = [int(el) for el in file.read().split()]
    print(sum(list_numbers))

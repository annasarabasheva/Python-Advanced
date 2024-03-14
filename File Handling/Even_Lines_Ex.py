import os

root_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(root_path, "text3.txt")
with open(file_path, "r") as file:
    list_lines = file.readlines()
    for idx in range(len(list_lines)):
        if idx % 2 == 0:
            result = list_lines[idx].split()
            reversed_result = f"{' '.join(result[::-1])}"
            reversed_result = reversed_result.replace("-", "@")
            reversed_result = reversed_result.replace(",", "@")
            reversed_result = reversed_result.replace(", ", "@")
            reversed_result = reversed_result.replace(".", "@")
            reversed_result = reversed_result.replace("!", "@")
            reversed_result = reversed_result.replace("?", "@")
            print(reversed_result)


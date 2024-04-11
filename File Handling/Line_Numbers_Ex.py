import os

root_path = os.path.dirname(os.path.abspath(__file__))
text_path = os.path.join(root_path, "text4.txt")
output_path = os.path.join(root_path, "output2.txt")

with open(text_path, "r") as text_file:
    list_lines = text_file.readlines()

with open(output_path, "w") as output_file:
    for idx in range(len(list_lines)):
        line = f"{' '.join(list_lines[idx].split())}"
        counter_letters = 0
        counter_symbols = 0
        for el in line:
            if el.isalpha():
                counter_letters += 1
            elif el == " ":
                continue
            else:
                counter_symbols += 1
        output_file.write(f"Line {idx+1}: {line} ({counter_letters})({counter_symbols})\n")
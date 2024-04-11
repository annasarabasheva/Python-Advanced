import os
import re

root_path = os.path.dirname(os.path.abspath(__file__))
words_path = os.path.join(root_path, "words.txt")
text_path = os.path.join(root_path, "text2.txt")
output_path = os.path.join(root_path, "output.txt")

with open(words_path, 'r') as words_file:
    words_list = words_file.read().lower().split()

with open(text_path, "r") as text_file:
    new_text_file = re.sub(r'[^\w]', ' ', text_file.read())
    text_file_list = new_text_file.lower().split()

with open(output_path, 'w') as output_file:
    dic = {}
    for word in words_list:
        if word in text_file_list:
            num = text_file_list.count(word)
            dic[word] = num
    for key, value in sorted(dic.items(), key=lambda x: x[1], reverse=True):
        output_file.write(f"{key} - {value}\n")



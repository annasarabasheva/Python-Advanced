text = input()

text_dic = {}
for el in text:
    if el not in text_dic:
        text_dic[el] = 1
    else:
        text_dic[el] += 1


for key, value in sorted(text_dic.items()):
    print(f"{key}: {value} time/s")

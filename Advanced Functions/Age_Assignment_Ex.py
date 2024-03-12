def age_assignment(*args, **kwargs):
    args = list(args)
    new_dic = {}
    for el in args:
        letter = el[0]
        for key, value in kwargs.items():
            if letter == key:
                new_dic[el] = value

    new_dic = sorted(new_dic.items(), key=lambda x: x[0])
    res = ""
    for i in range(len(new_dic)):
        res += f"{new_dic[i][0]} is {new_dic[i][1]} years old." + "\n"

    return res




print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
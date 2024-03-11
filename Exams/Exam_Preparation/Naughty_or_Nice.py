def naughty_or_nice_list(kids_list, *args, **kwargs):
    nice_list = []
    naughty_list = []
    not_found_list = []
    dic_santa = {}
    for idx in range(len(kids_list)):
        tuple = kids_list[idx]
        if tuple[0] not in dic_santa:
            dic_santa[tuple[0]] = []
        dic_santa[tuple[0]].append(tuple[1])

    for idx in range(len(args)):
        element = args[idx]
        new_element = element.split("-")
        key = int(new_element[0])
        status = new_element[1]
        if key in dic_santa:
            if len(dic_santa[key]) > 1:
                continue
            else:
                if status == "Nice":
                    nice_list.append(*dic_santa[key])
                    del dic_santa[key]
                elif status == "Naughty":
                    naughty_list.append(*dic_santa[key])
                    del dic_santa[key]

    second_dic_santa = {}
    for idx in range(len(kids_list)):
        tuple = kids_list[idx]
        if tuple[1] not in second_dic_santa:
            second_dic_santa[tuple[1]] = []
        second_dic_santa[tuple[1]].append(tuple[0])
    print(second_dic_santa)
    for key, value in kwargs.items():
        if key in second_dic_santa:
            if len(second_dic_santa[key]) > 1:
                continue
            else:
                if kwargs[key] == "Nice":
                    nice_list.append(key)
                    del second_dic_santa[key]

                elif kwargs[key] == "Naughty":
                    naughty_list.append(key)
                    del second_dic_santa[key]

    for key, value in dic_santa.items():
        not_found_list.append(dic_santa[key])
    print(nice_list)
    print(naughty_list)
    print(not_found_list)







#print(naughty_or_nice_list( [ (3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ], "3-Nice", "1-Naughty", Amy="Nice", Katy="Naughty", ))
print(naughty_or_nice_list( [ (7, "Peter"), (1, "Lilly"), (2, "Peter"), (12, "Peter"), (3, "Simon"), ], "3-Nice", "5-Naughty", "2-Nice", "1-Nice", ))
#print(naughty_or_nice_list( [ (6, "John"), (4, "Karen"), (2, "Tim"), (1, "Merry"), (6, "Frank"), ], "6-Nice", "5-Naughty", "4-Nice", "3-Naughty", "2-Nice", "1-Naughty", Frank="Nice", Merry="Nice", John="Naughty", ))
#[(3, 'Amy'), (1, 'Tom'), (7, 'George'), (3, 'Katy')]
#('3-Nice', '1-Naughty')
#{'Amy': 'Nice', 'Katy': 'Naughty'}
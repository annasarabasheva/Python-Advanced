def start_spring(**kwargs):
    new_dic = {}
    for key, value in kwargs.items():
        if value not in new_dic:
            new_dic[value] = []
        new_dic[value].append(key)
    new_dic_sorted = sorted(new_dic.items(), key=lambda x: (-len(x[1]), x[0]))
    new_new = {}
    for idx in range(len(new_dic_sorted)):
        element = new_dic_sorted[idx]
        new_new[element[0]] = sorted(element[1])
    result = ""
    for key, value in new_new.items():
        result += f"{key}:\n"
        for el in value:
            result += f"-{el}\n"
    return result

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

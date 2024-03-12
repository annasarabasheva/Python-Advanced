def grocery_store(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    res = ""
    for i in range(len(kwargs)):
        element = kwargs[i]
        res += f"{element[0]}: {element[-1]}" + "\n"
    return res




print(grocery_store( bread=5, pasta=12, eggs=12, ))
print(grocery_store( bread=2, pasta=2, eggs=20, carrot=1, ))
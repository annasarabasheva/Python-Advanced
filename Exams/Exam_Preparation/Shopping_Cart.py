def shopping_cart(*args):
    dic_products = {"Soup": [], "Pizza": [], "Dessert": []}
    for el in args:
        if el != "Stop":
            if el[0] == "Soup" and len(dic_products[el[0]]) == 3:
                continue
            elif el[0] == "Pizza" and len(dic_products[el[0]]) == 4:
                continue
            elif el[0] == "Dessert" and len(dic_products[el[0]]) == 2:
                continue
            if el[1] not in dic_products[el[0]]:
                dic_products[el[0]].append(el[1])
        else:
            break
    dic_products = sorted(dic_products.items(), key=lambda x: (-len(x[1]), x[0]))
    new_dic = {}
    for idx in range(len(dic_products)):
        element = dic_products[idx]
        new_dic[element[0]] = sorted(element[1])
    result = ""
    if len(new_dic["Pizza"]) == 0 and len(new_dic["Soup"]) == 0 and len(new_dic["Dessert"]) == 0:
        return "No products in the cart!"
    for key, value in new_dic.items():
        if value:
            result += f"{key}:\n"
            for el in value:
                result += f" - {el}\n"
        else:
            result += f"{key}:\n"
    return result

"""
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

print("------------------------------------------------------------------------------------------------------------")
"""
print(shopping_cart(
    ('Pizza', 'Pizza'),
    ('Pizza', 'guz'),
    ('Pizza', 'buz'),
    ('Pizza', 'Pizza'),
    ('Soup', 'guz'),
    'Stop'
))

def even_odd(*args):
    command = args[-1]
    pos_list = []
    neg_list = []
    args = args[:-1]
    for num in args:
        if num % 2 == 0:
            pos_list.append(num)
        else:
            neg_list.append(num)
    if command == "even":
        return pos_list
    elif command == "odd":
        return neg_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

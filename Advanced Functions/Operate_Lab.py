from functools import reduce


def operate(operator, *args):
    res = reduce(lambda a, b: eval(f"{a}{operator}{b}"), args)
    return res


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
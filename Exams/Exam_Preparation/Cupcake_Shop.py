def stock_availability(list, status, *args):
    if status == "delivery":
        for el in args:
            list.append(el)
    elif status == "sell":
        if len(args) == 0:
            list = list[1:]

        elif isinstance(args[0], int):
            for el in args:
                size = int(el)
                list = list[size:]

        elif isinstance(args[0], str):
            for el in args:
                if el in list:
                    list = [item for item in list if item != el]
    return list



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

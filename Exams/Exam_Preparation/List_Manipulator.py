def list_manipulator(num_list, *args):
    numbers = []
    commands = []
    result = []
    for el in args:
        if isinstance(el, int):
            numbers.append(el)
        else:
            commands.append(el)
    if commands[0] == "add" and commands[1] == "beginning":
        result = numbers + num_list
        return result
    elif commands[0] == "add" and commands[1] == "end":
        result = num_list + numbers
        return result

    elif commands[0] == "remove" and commands[1] == "beginning":
        if numbers:
            num_list = num_list[numbers[0]:]
            return num_list
        else:
            num_list = num_list[1:]
            return num_list
    elif commands[0] == "remove" and commands[1] == "end":
        if numbers:
            num_list = num_list[0:len(num_list) - numbers[0]]
            return num_list
        else:
            num_list = num_list[:-1]
            return num_list



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

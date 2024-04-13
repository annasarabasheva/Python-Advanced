first_set = {int(el) for el in input().split()}
second_set = {int(el) for el in input().split()}
n = int(input())
for i in range(n):
    line = input().split()
    command = line[0]
    position = line[1]
    if command == "Add":
        if position == "First":
            for el in line:
                if el.isnumeric():
                    first_set.add(int(el))
        elif position == "Second":
            for el in line:
                if el.isnumeric():
                    second_set.add(int(el))
    elif command == "Remove":
        if position == "First":
            for el in line:
                if el.isnumeric():
                    if int(el) in first_set:
                        first_set.remove(int(el))
        elif position == "Second":
            for el in line:
                if el.isnumeric():
                    if int(el) in second_set:
                        second_set.remove(int(el))
    elif command == "Check":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")

from collections import deque

quantity = int(input())
people = deque()
while True:
    name = input()
    if name == "Start":
        break
    people.append(name)


while True:
    command = input()
    if command == "End":
        print(f"{quantity} liters left")
        break

    command_arg = command.split()
    if len(command_arg) > 1:
        liters = int(command_arg[1])
        quantity += liters

    else:
        liters = int(command)
        if quantity >= liters:
            quantity -= liters
            print(f"{people.popleft()} got water")

        else:
            print(f"{people.popleft()} must wait")


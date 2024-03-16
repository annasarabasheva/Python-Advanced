rows = int(input())
matrix = [[int(el) for el in input().split()] for r in range(rows)]
while True:
    line = input()
    if line == "END":
        break
    command_arg = line.split()
    command = command_arg[0]
    row = int(command_arg[1])
    col = int(command_arg[2])
    value = int(command_arg[3])
    if row not in range(0, rows) or col not in range(0, rows):
        print("Invalid coordinates")
        continue
    if command == "Add":
        matrix[row][col] += value
    elif command == "Subtract":
        matrix[row][col] -= value
for el in matrix:
    print(*el)
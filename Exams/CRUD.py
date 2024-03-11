SIZE = 6
matrix = []
for row in range(SIZE):
    inner_line = input().split()
    matrix.append(inner_line)

line = input()
position = []
for el in line:
    if el.isdigit():
        position.append(int(el))
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
while True:
    line = input()
    if line == "Stop":
        break
    command_arg = line.split(', ')
    command = command_arg[0]
    direction = command_arg[1]
    row = position[0] + directions[direction][0]
    col = position[1] + directions[direction][1]
    position = [row, col]
    pos = matrix[row][col]
    if command == "Create":
        value = command_arg[2]
        if pos == ".":
            matrix[row][col] = value
    elif command == "Update":
        value = command_arg[2]
        if pos != ".":
            matrix[row][col] = value
    elif command == "Delete":
        if pos != ".":
            matrix[row][col] = "."
    elif command == "Read":
        if pos != ".":
            print(matrix[row][col])

print(*[' '.join(row) for row in matrix], sep='\n')
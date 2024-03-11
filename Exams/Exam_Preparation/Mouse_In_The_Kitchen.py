ROW, COL = [int(el) for el in input().split(',')]
matrix = []
mouse_pos = []
total_cheese = 0
for row in range(ROW):
    inner_line = list(input())
    number_of_cheese = inner_line.count("C")
    total_cheese += number_of_cheese
    matrix.append(inner_line)
    if "M" in inner_line:
        mouse_pos = [row, inner_line.index("M")]
        matrix[mouse_pos[0]][mouse_pos[1]] = "*"


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    direction = input()
    if direction == "danger":
        if total_cheese > 0:
            matrix[mouse_pos[0]][mouse_pos[1]] = "M"
            print("Mouse will come back later!")
        break
    row = mouse_pos[0] + directions[direction][0]
    col = mouse_pos[1] + directions[direction][1]
    if not (0 <= row < ROW and 0 <= col < COL):
        matrix[mouse_pos[0]][mouse_pos[1]] = "M"
        print("No more cheese for tonight!")
        break

    position = matrix[row][col]
    if position == "C":
        mouse_pos = [row, col]
        matrix[row][col] = "*"
        total_cheese -= 1
        if total_cheese == 0:
            matrix[row][col] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif position == "T":
        mouse_pos = [row, col]
        matrix[row][col] = "M"
        print("Mouse is trapped!")
        break
    elif position == "@":
        continue
    elif position == "*":
        mouse_pos = [row, col]


print(*[''.join(row) for row in matrix], sep='\n')
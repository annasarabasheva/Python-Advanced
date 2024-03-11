SIZE = int(input())
matrix = []
snake_pos = []
for r in range(SIZE):
    inner_line = list(input())
    matrix.append(inner_line)
    if "S" in inner_line:
        snake_pos = [r, inner_line.index("S")]
        matrix[r][snake_pos[1]] = "."

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
food_quantity = 0
enough_food = False
while True:
    direction = input()
    row = snake_pos[0] + directions[direction][0]
    col = snake_pos[1] + directions[direction][1]
    if 0 <= row < SIZE and 0 <= col < SIZE:
        snake_pos = [row, col]
        position = matrix[row][col]
        if position == "*":
            food_quantity += 1
            matrix[row][col] = "."
        elif position == "B":
            matrix[row][col] = "."
            for row in range(SIZE):
                if "B" in matrix[row]:
                    snake_pos = [row, matrix[row].index("B")]
                    matrix[snake_pos[0]][snake_pos[1]] = "."
        elif position == "-":
            matrix[row][col] = "."
        if food_quantity >= 10:
            enough_food = True
            matrix[row][col] = "S"
            break
    else:
        matrix[snake_pos[0]][snake_pos[1]] = "."
        print("Game over!")
        break

if enough_food:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")
print(*[''.join(row) for row in matrix], sep='\n')
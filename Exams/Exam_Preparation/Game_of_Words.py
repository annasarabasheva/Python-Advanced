word = input()
SIZE = int(input())
matrix = []
random_pos = []
for row in range(SIZE):
    inner_line = list(input())
    matrix.append(inner_line)
    if "P" in inner_line:
        random_pos = [row, matrix[row].index("P")]
        matrix[random_pos[0]][random_pos[1]] = "-"

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

num = int(input())
for i in range(num):
    direction = input()
    row = random_pos[0] + directions[direction][0]
    col = random_pos[1] + directions[direction][1]
    if 0 <= row < SIZE and 0 <= col < SIZE:
        position = matrix[row][col]
        random_pos = [row, col]
        if position.isalpha():
            word += position
            matrix[row][col] = "-"
    else:
        if word:
            word = word[0:-1]
        else:
            continue

matrix[random_pos[0]][random_pos[1]] = "P"
print(f'{word}')
print(*[''.join(row) for row in matrix], sep='\n')




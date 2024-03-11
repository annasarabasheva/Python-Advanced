from math import floor


def move_opposite(position, direction, field_size):
    row, col = position
    if direction == 'up':
        row = row % field_size
    elif direction == 'down':
        row = row % field_size
    elif direction == 'left':
        col = col % field_size
    elif direction == 'right':
        col = col % field_size
    return (row, col)


SIZE = int(input())
matrix = []
player_pos = []
for row in range(SIZE):
    inner_line = input().split()
    matrix.append(inner_line)
    if "P" in inner_line:
        player_pos = [row, matrix[row].index('P')]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
path = [player_pos]
collected_coins = 0
while True:
    direction = input()
    if direction not in ["up", "down", "left", "right"]:
        continue
    row = player_pos[0] + directions[direction][0]
    col = player_pos[1] + directions[direction][1]
    if 0 <= row < SIZE and 0 <= col < SIZE:
        player_pos = [row, col]
        position = matrix[row][col]
    else:
        row, col = move_opposite([row, col], direction, SIZE)
        player_pos = [row, col]
        position = matrix[row][col]

    path.append(player_pos)

    if position.isdigit():
        collected_coins += int(position)
        matrix[row][col] = '.'

    elif position == "X":
        print(f"Game over! You've collected {floor(collected_coins * 0.5)} coins.")
        break
    if collected_coins >= 100:
        print(f"You won! You've collected {collected_coins} coins.")
        break

print("Your path:")
for el in path:
    print(el)
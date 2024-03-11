ROW, COL = [int(el) for el in input().split()]
field = []
b_pos = []
for r in range(ROW):
    inner_line = input().split()
    field.append(inner_line)
    if "B" in inner_line:
        b_pos = [r, field[r].index("B")]
        field[r][b_pos[1]] = '-'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
touched_opponents = 0
game_over = False
moves = 0
while True:
    command = input()
    if command == "Finish":
        break
    row = b_pos[0] + directions[command][0]
    col = b_pos[1] + directions[command][1]

    if not (0 <= row < ROW and 0 <= col < COL):
        continue

    position = field[row][col]
    if position == "O":
        continue

    b_pos = [row, col]
    field[row][col] = '-'
    if position == "P":
        touched_opponents += 1
        moves += 1
    elif position == "-":
        moves += 1

    if touched_opponents == 3:
        game_over = True
        break


print(f"Game over!\nTouched opponents: {touched_opponents} Moves made: {moves}")
size = int(input())
commands = input().split(', ')
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
field = []
s_pos = []
for row in range(size):
    inner_line = list(input())
    field.append(inner_line)
    if 's' in inner_line:
        s_pos = [row, field[row].index('s')]
        field[row][s_pos[1]] = '*'

hazelnuts = 0
traps_field = False
for command in commands:
    row = s_pos[0] + directions[command][0]
    col = s_pos[1] + directions[command][1]
    if not (0 <= row < size and 0 <= col < size):
        print("The squirrel is out of the field.")
        traps_field = True
        break
    s_pos = [row, col]
    position = field[row][col]
    field[row][col] = '*'
    if position == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        traps_field = True
        break

    elif position == "h":
        hazelnuts += 1

    if hazelnuts == 3:

        print("Good job! You have collected all hazelnuts!")
        break

if not traps_field and hazelnuts < 3:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
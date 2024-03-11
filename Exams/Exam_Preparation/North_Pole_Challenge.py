def move(position, direction, r, c):
    row, col = position
    if direction == 'up':
        row = row % r
    elif direction == 'down':
        row = row % r
    elif direction == 'left':
        col = col % c
    elif direction == 'right':
        col = col % c
    return (row, col)


ROW, COL = [int(el) for el in input().split(', ')]

workshop = []
my_position = []
for r in range(ROW):
    inner_line = input().split()
    workshop.append(inner_line)
    if "Y" in inner_line:
        my_position = [r, workshop[r].index("Y")]
        workshop[my_position[0]][my_position[1]] = "x"

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
decorations = 0
gifts = 0
cookies = 0
game_over = False
while True:
    line = input()
    if line == "End":
        workshop[my_position[0]][my_position[1]] = "Y"
        break
    command_arg = line.split('-')
    direction = command_arg[0]
    steps = int(command_arg[1])

    row = my_position[0] + (directions[direction][0] * steps)
    col = my_position[1] + (directions[direction][1] * steps)


    if 0 <= row < ROW and 0 <= col < COL:
        my_position = [row, col]

    else:
        row, col = move([row, col], direction, ROW, COL)
        my_position = [row, col]

    position = workshop[row][col]
    if position == "D":
        decorations += 1
    elif position == "G":
        gifts += 1
    elif position == "C":
        cookies += 1

"""
6, 5
. . . . .
C . . G .
. C . . .
G . . C .
. D . . D
Y . . . G
left-3
up-1
left-2
right-7
up-1
End
"""

"""
6, 5
. . . . .
C . . G .
. C . . .
G . . C .
. D . . D
Y . . . G
right-2
End
"""

print(f"You've collected:\n- {decorations} Christmas decorations\n- {gifts} Gifts\n- {cookies} Cookies")
print(*[' '.join(row) for row in workshop], sep='\n')

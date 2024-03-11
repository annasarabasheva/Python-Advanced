ROW, COL = [int(el) for el in input().split(', ')]
workshop = []
my_position = []


def movement(row, col, direction, steps):
    counter = 1
    tempCol = col
    tempRow = row
    print(f"currentPosition is {row}-{col}")
    while counter <= steps:
        if col > COL - 1:
            col = 0
        elif col < 0:
            col = COL - 1
        elif row > ROW - 1:
            row = 0
        elif row < 0:
            row = ROW - 1

        row = tempRow + (directions[direction][0] * counter)
        col = tempCol + (directions[direction][1] * counter)

        print(f"POSITION TO BE CHANGED IS {row}-{col} | COUNTER IS {counter}")
        counter += 1
        workshop[row][col] = "x"

    my_position[0] = row
    my_position[1] = col
    print(*[' '.join(row) for row in workshop], sep='\n')


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

while True:
    line = input()
    if line == "End":
        workshop[my_position[0]][my_position[1]] = "Y"
        break
    command_arg = line.split('-')
    direction = command_arg[0]
    steps = int(command_arg[1])

    row = my_position[0]
    col = my_position[1]

    movement(row, col, direction, steps)
"""
6, 5
. . . . .
C . . G .
. C . . .
G . . C .
. D . . D
Y . . . G
right-4
End
"""

print(*[' '.join(row) for row in workshop], sep='\n')

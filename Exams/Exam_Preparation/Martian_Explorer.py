def move_rover(position, direction, field_size):
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

rover_position = []
field = []
for row in range(6):
    inner_field = input().split()
    field.append(inner_field)
    if "E" in inner_field:
        rover_position = [row, field[row].index("E")]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
size = 6
water = 0
metal = 0
concrete = 0
broken_rover = False
line = input()
commands = line.split(', ')
for idx in range(len(commands)):
    command = commands[idx]
    row = rover_position[0] + directions[command][0]
    col = rover_position[1] + directions[command][1]

    if 0 <= row < 6 and 0 <= col < 6:
        rover_position = [row, col]
        position = field[row][col]
        if position in ["W", "M", "C"]:
            if position == "W":
                water += 1
                print(f"Water deposit found at ({row}, {col})")
            elif position == "M":
                metal += 1
                print(f"Metal deposit found at ({row}, {col})")
            elif position == "C":
                concrete += 1
                print(f"Concrete deposit found at ({row}, {col})")
        elif position == "R":
            print(f"Rover got broken at ({row}, {col})")
            broken_rover = True
            break
    else:
        row, col = move_rover([row, col], command, size)
        rover_position = [row, col]
        position = field[row][col]
        if position in ["W", "M", "C"]:
            if position == "W":
                water += 1
                print(f"Water deposit found at ({row}, {col})")
            elif position == "M":
                metal += 1
                print(f"Metal deposit found at ({row}, {col})")
            elif position == "C":
                concrete += 1
                print(f"Concrete deposit found at ({row}, {col})")
        elif position == "R":
            print(f"Rover got broken at ({row}, {col})")
            broken_rover = True
            break
    if broken_rover:
        break


if water > 0 and metal > 0 and concrete > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
from collections import deque
names = deque(input().split(', '))
maze = []
for row in range(6):
    inner_maze = input().split()
    maze.append(inner_maze)
positions = {}
while True:
    command = input()
    player = names[0]
    if player not in positions:
        positions[player] = []
    if positions[player]:
        if positions[player][-1] == "W":
            positions[player][-1] = "."
            names.rotate()
            continue
    player_position = []
    for el in command:
        if el.isdigit():
            player_position.append(int(el))
    position = maze[player_position[0]][player_position[1]]
    if position == "E":
        print(f"{player} found the Exit and wins the game!")
        break
    elif position == "T":
        print(f"{player} is out of the game! The winner is {names[1]}.")
        break
    elif position == "W":
        print(f"{player} hits a wall and needs to rest.")
        positions[player].append("W")
    elif position == ".":
        positions[player].append(".")
    names.rotate()


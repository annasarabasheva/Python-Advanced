from collections import deque

players = deque(input().split(', '))
SIZE = 7
dartboard = []
for row in range(SIZE):
    inner_line = input().split()
    dartboard.append(inner_line)

players_scores_throws = {players[0]: [501, 0], players[1]: [501, 0]}

while True:
    line = input()
    coordinates = []
    players_scores_throws[players[0]][1] += 1
    for el in line:
        if el.isdigit():
            coordinates.append(int(el))
    if 0 <= coordinates[0] < SIZE and 0 <= coordinates[1] < SIZE:
        position = dartboard[coordinates[0]][coordinates[1]]
        if position.isdigit():
            players_scores_throws[players[0]][0] -= int(position)
        elif position == "B":
            break
        elif position == "D" or position == "T":
            sum_numbers = int(dartboard[coordinates[0]][0]) + int(dartboard[coordinates[0]][SIZE - 1]) + int(
                dartboard[0][coordinates[1]]) + int(dartboard[SIZE - 1][coordinates[1]])
            if position == "D":
                sum_numbers *= 2
            elif position == "T":
                sum_numbers *= 3
            players_scores_throws[players[0]][0] -= int(sum_numbers)

        if players_scores_throws[players[0]][0] <= 0:
            break

    players.rotate()


print(f"{players[0]} won the game with {players_scores_throws[players[0]][1]} throws!")
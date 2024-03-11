size = int(input())
battlefield = []
s_pos = []
for row in range(size):
    inner_field = list(input())
    battlefield.append(inner_field)
    if "S" in inner_field:
        s_pos = [row, battlefield[row].index("S")]
        battlefield[row][s_pos[1]] = '-'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
mines_hit = 0
destroyed_cruisers = 0
while True:
    command = input()
    row = s_pos[0] + directions[command][0]
    col = s_pos[1] + directions[command][1]

    position = battlefield[row][col]
    if position == "-":
        s_pos = [row, col]
        battlefield[row][col] = "S"
    elif position == "*":
        mines_hit += 1
        if mines_hit < 3:
            s_pos = [row, col]
            battlefield[row][col] = "-"
        else:
            s_pos = [row, col]
            battlefield[row][col] = "S"
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            break
    elif position == "C":
        destroyed_cruisers += 1
        if destroyed_cruisers < 3:
            s_pos = [row, col]
            battlefield[row][col] = "-"
        else:
            s_pos = [row, col]
            battlefield[row][col] = "S"
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break
    battlefield[row][col] = "-"

print(*[''.join(row) for row in battlefield], sep='\n')
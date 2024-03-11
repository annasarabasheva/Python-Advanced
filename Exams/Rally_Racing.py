size = int(input())
racing_number = input()
matrix = []
for row in range(size):
    inner_line = input().split()
    matrix.append(inner_line)
car_pos = [0, 0]
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
sum_kilometers = 0
while True:
    command = input()
    if command == "End":
        matrix[car_pos[0]][car_pos[1]] = "C"
        print(f"Racing car {racing_number} DNF.")
        break
    row = car_pos[0] + directions[command][0]
    col = car_pos[1] + directions[command][1]

    position = matrix[row][col]
    if position == ".":
        car_pos = [row, col]
        matrix[row][col] = "."
        sum_kilometers += 10
    elif position == "T":
        matrix[row][col] = "."
        for row in range(size):
            if "T" in matrix[row]:
                car_pos = [row, matrix[row].index('T')]
                matrix[car_pos[0]][car_pos[1]] = "."

        sum_kilometers += 30
    elif position == "F":
        sum_kilometers += 10
        car_pos = [row, col]
        matrix[car_pos[0]][car_pos[1]] = "C"
        print(f"Racing car {racing_number} finished the stage!")
        break


print(f"Distance covered {sum_kilometers} km." )
print(*[''.join(row) for row in matrix], sep='\n')
rows, cols = [int(el) for el in input().split()]
matrix = []
for r in range(rows):
    inner_list = list(input().split())
    matrix.append(inner_list)
while True:
    line = input()
    if line == "END":
        break
    command_arg = line.split()
    if len(command_arg) != 5:
        print("Invalid input!")
        continue
    command = command_arg[0]
    row1, col1 = int(command_arg[1]), int(command_arg[2])
    row2, col2 = int(command_arg[3]), int(command_arg[4])
    if command != "swap" or row1 > rows or col1 > cols or row2 > rows or col2 > cols or row1 < 0 or col1 < 0 or row2 < 0 or col2 < 0:
        print("Invalid input!")
        continue
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for i in range(len(matrix)):
        print(*matrix[i])



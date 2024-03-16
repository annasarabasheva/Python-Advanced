n = int(input())
matrix = []
for i in range(n):
    inner_line = list(input())
    matrix.append(inner_line)

symbol = input()
positions = []
for r in range(n):
    if len(positions) == 2:
        break
    for c in range(n):
        element = matrix[r][c]
        if element == symbol:
            positions.append(r)
            positions.append(c)
            break

if positions:
    print(tuple(positions))
else:
    print(f"{symbol} does not occur in the matrix")
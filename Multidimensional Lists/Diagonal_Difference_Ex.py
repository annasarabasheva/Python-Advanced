rows = int(input())
matrix = []
for row_idx in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

primary_diagonal = [matrix[i][i] for i in range(rows)]
second_diagonal = [matrix[rows-1-i][i] for i in range(rows - 1, -1, -1)]
difference = abs(sum(primary_diagonal) - sum(second_diagonal))
print(difference)
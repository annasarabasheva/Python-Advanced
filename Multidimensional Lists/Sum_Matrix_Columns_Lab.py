rows, cols = [int(el) for el in input().split(', ')]
matrix = []
for row_idx in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

sums_cols =[]
for col_idx in range(cols):
    sum_cols = 0
    for rol_idx in range(rows):
        element = matrix[rol_idx][col_idx]
        sum_cols += element
        if rol_idx == rows - 1:
            sums_cols.append(sum_cols)

for el in sums_cols:
    print(el)
rows = int(input())
matrix = []
for row_idx in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

numbers = []
for r_idx in range(rows):
    for c_idx in range(len(matrix[r_idx])):
        if r_idx == c_idx:
            element = matrix[r_idx][c_idx]
            numbers.append(element)
print(sum(numbers))
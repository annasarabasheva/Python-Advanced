rows, cols = [int(el) for el in input().split(", ")]
matrix = []
sum_numbers = 0
for row_index in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    sum_numbers += sum(inner_list)
    matrix.append(inner_list)

print(sum_numbers)
print(matrix)
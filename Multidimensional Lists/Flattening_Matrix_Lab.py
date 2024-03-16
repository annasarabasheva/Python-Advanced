rows = int(input())

flatten_matrix = []
for row_idx in range(rows):
    numbers = [int(el) for el in input().split(', ')]
    flatten_matrix.extend(numbers)

print(flatten_matrix)
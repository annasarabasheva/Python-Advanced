rows, cols = [int(el) for el in input().split()]
matrix = []
for r in range(rows):
    inner_line = [str(el) for el in input().split()]
    matrix.append(inner_line)
counter = 0
for r_idx in range(rows - 1):
    for c_idx in range(cols - 1):
        sum_elements = 0
        first_element = matrix[r_idx][c_idx]
        next_element = matrix[r_idx][c_idx + 1]
        upper_element = matrix[r_idx + 1][c_idx]
        next_upper_element = matrix[r_idx + 1][c_idx + 1]
        if first_element == next_element == upper_element == next_upper_element:
            counter += 1
print(counter)
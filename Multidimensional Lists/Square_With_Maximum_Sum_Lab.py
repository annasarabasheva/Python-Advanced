rows, cols = [int(el) for el in input().split(', ')]
matrix = []
for r in range(rows):
    inner_line = [int(el) for el in input().split(', ')]
    matrix.append(inner_line)
max_sum = float('-inf')
elements = []
for r_idx in range(rows - 1):
    for c_idx in range(cols - 1):
        sum_elements = 0
        first_element = matrix[r_idx][c_idx]
        next_element = matrix[r_idx][c_idx + 1]
        upper_element = matrix[r_idx + 1][c_idx]
        next_upper_element = matrix[r_idx + 1][c_idx + 1]
        sum_elements += first_element + next_element + upper_element + next_upper_element
        if sum_elements > max_sum:
            elements.clear()
            max_sum = sum_elements
            elements.append([first_element, next_element])
            elements.append([upper_element, next_upper_element])
for i in range(2):
    print(*elements[i])
print(max_sum)
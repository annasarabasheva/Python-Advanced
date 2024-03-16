rows, cols = [int(el) for el in input().split()]
matrix = []
for r in range(rows):
    inner_line = [int(el) for el in input().split()]
    matrix.append(inner_line)
max_sum = float('-inf')
elements = []
for r_idx in range(rows - 2):
    for c_idx in range(cols - 2):
        sum_elements = 0
        first_element = matrix[r_idx][c_idx]
        second_right_element = matrix[r_idx][c_idx + 1]
        third_right_element = matrix[r_idx][c_idx + 2]
        down_element = matrix[r_idx + 1][c_idx]
        second_down_right_element = matrix[r_idx + 1][c_idx + 1]
        third_down_right_element = matrix[r_idx + 1][c_idx + 2]
        last_down_element = matrix[r_idx + 2][c_idx]
        last_second_down_element = matrix[r_idx + 2][c_idx + 1]
        last_third_down_element = matrix[r_idx + 2][c_idx + 2]
        sum_elements += first_element + second_right_element + third_right_element + down_element + second_down_right_element + third_down_right_element + last_down_element + last_second_down_element + last_third_down_element
        if sum_elements > max_sum:
            elements.clear()
            max_sum = sum_elements
            elements.append([first_element, second_right_element, third_right_element])
            elements.append([down_element, second_down_right_element, third_down_right_element])
            elements.append([last_down_element, last_second_down_element, last_third_down_element])
print(f"Sum = {max_sum}")
for i in range(3):
    print(*elements[i])

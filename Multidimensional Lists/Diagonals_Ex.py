rows = int(input())
matrix = []
for row_idx in range(rows):
    inner_list = [int(el) for el in input().split(', ')]
    matrix.append(inner_list)

primary_diagonal = []
for r_idx in range(rows):
    for c_idx in range(len(matrix[r_idx])):
        if r_idx == c_idx:
            element = matrix[r_idx][c_idx]
            primary_diagonal.append(element)

second_diagonal = [matrix[rows-1-i][i] for i in range(rows-1,-1,-1)]  #comprehension

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in second_diagonal])}. Sum: {sum(second_diagonal)}")

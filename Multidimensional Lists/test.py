matrix = [[-2,  5,  3,  2],
          [9, -6,  5,  1],
          [3,  2,  7,  3],
          [-1,  8, -4,  8]]

l = len(matrix[0])
print([matrix[i][i] for i in range(l)])              # [-2, -6, 7,  8]
print([matrix[l-1-i][i] for i in range(l-1,-1,-1)])  # [ 2,  5, 2, -1]
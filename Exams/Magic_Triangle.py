def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    if n == 1:
        return triangle[:1]
    elif n == 2:
        return triangle

    for i in range(2, n):
        row = [1]  # Start each row with 1
        prev_row = triangle[i - 1]

        for j in range(1, i):
            # Calculate the sum of the two numbers above
            num = prev_row[j - 1] + prev_row[j]
            row.append(num)

        row.append(1)  # End each row with 1
        triangle.append(row)
    return triangle


get_magic_triangle(5)
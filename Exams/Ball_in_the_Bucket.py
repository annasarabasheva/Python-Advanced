SIZE = 6
matrix = []
for row in range(SIZE):
    inner_line = input().split()
    matrix.append(inner_line)
sum_points = 0
for i in range(3):
    position = input()
    my_position = []
    for el in position:
        if el.isdigit():
            my_position.append(int(el))
    if 0 <= my_position[0] < SIZE and 0 <= my_position[1] < SIZE:
        if matrix[my_position[0]][my_position[1]] == "B":
            for r in range(SIZE):
                element = matrix[r][my_position[1]]
                if element.isdigit():
                    sum_points += int(element)

            matrix[my_position[0]][my_position[1]] = "x"

if sum_points < 100:
    print(f"Sorry! You need {100 - sum_points} points more to win a prize.")
elif 100 <= sum_points <= 199:
    print(f"Good job! You scored {sum_points} points, and you've won Football.")
elif 200 <= sum_points <= 299:
    print(f"Good job! You scored {sum_points} points, and you've won Teddy Bear.")
elif sum_points >= 300:
    print(f"Good job! You scored {sum_points} points, and you've won Lego Construction Set.")





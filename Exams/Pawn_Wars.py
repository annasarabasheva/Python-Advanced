from math import ceil

SIZE = 8
board = [input().split() for r in range(SIZE)]

white_position = ()
black_position = ()
for r in range(SIZE-1,-1,-1):
    for c in range(SIZE):
        if board[r][c] == "w":
            print(f"ROW IS {r} | COLUM IS {c} ")

            white_position = (c + 1, 8-r)

        elif board[r][c] == "b":
            black_position = (c + 1, 8-r)

print(white_position)
print(black_position)

if abs(white_position[0] - black_position[0]) > 1:
    left_rows_white = SIZE - white_position[1]
    left_rows_black = abs(black_position[1] - 1)
    if left_rows_white > left_rows_black:
        print(f"Game over! Black pawn is promoted to a queen at {chr(96 + black_position[0])}1.")
    else:
        print(f"Game over! White pawn is promoted to a queen at {chr(96 + white_position[0])}8.")

else:
    if abs(white_position[1] - black_position[1]) % 2 == 0:
        print(f"Game over! Black pawn is promoted to a queen at {chr(96 + white_position[0])}{ceil(white_position+white_position[1]/2)}.")
    else:
        print(f"Game over! White pawn is promoted to a queen at {chr(96 + black_position[0])}{ceil(black_position[1]/2)}.")


"""
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
w - - - - - - -
- - - - - - - -
- - - - - - - -
"""

"""
- - - - - - - -
- - - - b - - -
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - w - - - -
- - - - - - - -
- - - - - - - -
"""
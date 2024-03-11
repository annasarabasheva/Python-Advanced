from collections import deque

seats = input().split(', ')
numbers_first = deque([int(el) for el in input().split(", ")])
numbers_second = deque([int(el) for el in input().split(", ")])
matched_seats = []
rotations = 0

while numbers_first and numbers_second and (rotations < 10 or len((matched_seats)) < 3):
    first_number = numbers_first.popleft()
    last_number = numbers_second.pop()
    sum_numbers = first_number + last_number
    letter = chr(sum_numbers)
    first_combination = f"{str(first_number)}{letter}"
    second_combination = f"{str(last_number)}{letter}"
    if first_combination not in seats and second_combination not in seats:
        numbers_first.append(first_number)
        numbers_second.appendleft(last_number)

    else:
        for el in seats:
            if (el == first_combination) or (el == second_combination):
                if el not in matched_seats:
                    matched_seats.append(el)

    rotations += 1
print(f"Seat matches: {', '.join(matched_seats)}\nRotations count: {rotations}")

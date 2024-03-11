from collections import deque

daily_portions = deque([int(el) for el in input().split(', ')])
daily_stamina = deque([int(el) for el in input().split(', ')])
mountains = deque([("Vihren", 80), ("Kutelo",90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)])

conquered_peaks = []
while daily_stamina and daily_portions:
    portion = daily_portions.pop()
    stamina = daily_stamina.popleft()
    mountain = mountains.popleft()
    name = mountain[0]
    difficulty_level = mountain[1]
    sum_both = stamina + portion
    if sum_both >= difficulty_level:
        conquered_peaks.append(name)
    else:
        mountains.appendleft(mountain)

    if not mountains:
        break


if not mountains:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    for el in conquered_peaks:
        print(el)

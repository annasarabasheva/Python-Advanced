from collections import deque

males = deque([int(el) for el in input().split()])
females = deque([int(el) for el in input().split()])
matches = 0
while males and females:
    male = males.pop()
    female = females.popleft()
    if male <= 0 and female > 0:
        females.appendleft(female)
        continue
    elif male > 0 and female <= 0:
        males.append(male)
        continue
    elif male <= 0 and female <= 0:
        continue
    if male % 25 == 0 and female % 25 != 0:
        females.appendleft(female)
        second_male = males.pop()
        continue
    elif female % 25 == 0 and male % 25 != 0:
        males.append(male)
        second_female = females.popleft()
        continue
    elif male % 25 == 0 and female % 25 == 0:
        second_male = males.pop()
        second_female = females.popleft()
        continue
    if male == female:
        matches += 1
    else:
        male -= 2
        males.append(male)


print(f"Matches: {matches}")
if not males:
    print("Males left: none")
else:
    males.reverse()
    print(f"Males left: {', '.join([str(el) for el in males])}")
if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join([str(el) for el in females])}")
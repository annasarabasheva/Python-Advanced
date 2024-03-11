from collections import deque

milligrams = deque([int(el) for el in input().split(', ')])
energy_drinks = deque([int(el) for el in input().split(', ')])
maximum_caffeine = 300
total_caffeine = 0
while milligrams and energy_drinks:
    milligram = milligrams.pop()
    drink = energy_drinks.popleft()
    combination = milligram * drink
    if combination <= maximum_caffeine:
        total_caffeine += combination
        maximum_caffeine -= combination
    else:
        energy_drinks.append(drink)
        total_caffeine = max((total_caffeine - 30), 0)
        if total_caffeine == 0:
            maximum_caffeine = 300
        else:
            maximum_caffeine = min(300, maximum_caffeine + 30)


if energy_drinks:
    print(f"Drinks left: {', '.join([str(el) for el in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
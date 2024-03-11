
from collections import deque

materials = deque([int(el) for el in input().split()])
magic_levels = deque([int(el) for el in input().split()])
gifts = {'Gemstone': 0, "Porcelain Sculpture": 0, "Gold": 0, "Diamond Jewellery": 0}
while materials and magic_levels:
    material = materials.pop()
    magic_level = magic_levels.popleft()
    sum_materials = material + magic_level
    if 100 <= sum_materials <= 199:
        gifts["Gemstone"] += 1
    elif 200 <= sum_materials <= 299:
        gifts["Porcelain Sculpture"] += 1
    elif 300 <= sum_materials <= 399:
        gifts["Gold"] += 1
    elif 400 <= sum_materials <= 499:
        gifts["Diamond Jewellery"] += 1

    elif sum_materials < 100:
        if sum_materials % 2 == 0:
            material *= 2
            magic_level *= 3
            new_sum = material + magic_level
        else:
            material *= 2
            magic_level *= 2
            new_sum = material + magic_level
        if 100 <= new_sum <= 199:
            gifts["Gemstone"] += 1
        elif 200 <= new_sum <= 299:
            gifts["Porcelain Sculpture"] += 1
        elif 300 <= new_sum <= 399:
            gifts["Gold"] += 1
        elif 400 <=new_sum <= 499:
            gifts["Diamond Jewellery"] += 1

    elif sum_materials > 499:
        material /= 2
        magic_level /= 2
        new_sum = material + magic_level
        if 100 <= new_sum <= 199:
            gifts["Gemstone"] += 1
        elif 200 <= new_sum <= 299:
            gifts["Porcelain Sculpture"] += 1
        elif 300 <= new_sum <= 399:
            gifts["Gold"] += 1
        elif 400 <= new_sum <= 499:
            gifts["Diamond Jewellery"] += 1

if (gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0) or ((gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0)):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(el) for el in materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(el) for el in magic_levels)}")

for key, value in sorted(gifts.items()):
    if value > 0:
        print(f"{key}: {value}")
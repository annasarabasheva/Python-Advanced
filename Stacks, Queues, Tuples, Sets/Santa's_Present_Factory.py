from collections import deque
materials = deque([int(el) for el in input().split()])
magic_level = deque([int(el) for el in input().split()])
magic_needed = {
    "Doll": [150, 0],
    "Wooden train": [250, 0],
    "Teddy bear": [300, 0],
    "Bicycle": [400, 0]
}
while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()
    if material == 0 and magic != 0:
        magic_level.appendleft(magic)
        continue
    elif magic == 0 and material != 0:
        materials.append(material)
        continue
    elif magic == 0 and material == 0:
        continue
    total_magic_level = material * magic
    for key, value in magic_needed.items():
        if magic_needed[key][0] == total_magic_level:
            magic_needed[key][1] += 1
    if total_magic_level < 0:
        sum_values = material + magic
        materials.append(sum_values)
    elif total_magic_level not in [150, 250, 300, 400] and total_magic_level > 0:
        materials.append(material + 15)


if (magic_needed["Doll"][1] > 0 and magic_needed["Wooden train"][1] > 0) or (magic_needed["Teddy bear"][1] > 0 and magic_needed["Bicycle"][1] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    materials.reverse()
    print(f"Materials left: {', '.join(str(el) for el in materials)}")

if magic_level:
    print(f"Magic left: {', '.join(str(el) for el in magic_level)}")

for key, value in sorted(magic_needed.items()):
    if magic_needed[key][1] > 0:
        print(f"{key}: {magic_needed[key][1]}")
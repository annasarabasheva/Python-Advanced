from collections import deque

elf_energy = deque([int(el) for el in input().split()])
box_materials = deque([int(el) for el in input().split()])
times = 0
toys = 0
used_energy = 0


def not_enough_energy(current_elf_energy):
    current_elf_energy = current_elf_energy * 2
    elf_energy.append(current_elf_energy)
    box_materials.append(current_material)


while elf_energy and box_materials:
    current_elf_energy = elf_energy.popleft()
    if current_elf_energy < 5:
        continue
    current_material = box_materials.pop()
    times += 1

    if times % 15 == 0:
        if current_elf_energy >= current_material * 2:
            used_energy += current_material * 2
            current_elf_energy -= current_material * 2
            elf_energy.append(current_elf_energy)
        else:
            not_enough_energy(current_elf_energy)
        continue

    if times % 3 == 0:
        if current_elf_energy >= current_material * 2:
            used_energy += current_material * 2
            current_elf_energy -= current_material * 2 - 1
            elf_energy.append(current_elf_energy)
            toys += 2
        else:
            not_enough_energy(current_elf_energy)
        continue

    if times % 5 == 0:
        if current_elf_energy >= current_material:
            used_energy += current_material
            current_elf_energy -= current_material
            elf_energy.append(current_elf_energy)
        else:
            not_enough_energy(current_elf_energy)
        continue

    if current_elf_energy >= current_material:
        used_energy += current_material
        current_elf_energy -= current_material - 1
        elf_energy.append(current_elf_energy)
        toys += 1
    else:
        not_enough_energy(current_elf_energy)


print(f"Toys: {toys}")
print(f"Energy: {used_energy}")
if elf_energy:
    print(f"Elves left: {', '.join(str(el) for el in elf_energy)}")
if box_materials:
    print(f"Boxes left: {', '.join(str(el) for el in box_materials)}")
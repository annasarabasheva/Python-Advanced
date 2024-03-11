from collections import deque

textiles = deque([int(el) for el in input().split()])
medicaments = deque([int(el) for el in input().split()])

dic_medicaments = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    sum_both = textile + medicament
    if sum_both in [30, 40, 100]:
        if sum_both == 30:
            dic_medicaments["Patch"] += 1
        elif sum_both == 40:
            dic_medicaments["Bandage"] += 1
        elif sum_both == 100:
            dic_medicaments["MedKit"] += 1
    elif sum_both < 100:
        medicament += 10
        medicaments.append(medicament)
    elif sum_both > 100:
        dic_medicaments["MedKit"] += 1
        rest = sum_both - 100
        medicament_new = medicaments.pop()
        medicament_new += rest
        medicaments.append(medicament_new)


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

dic_medicaments = sorted(dic_medicaments.items(), key=lambda x: (-x[1], x[0]))
for idx in range(len(dic_medicaments)):
    element = dic_medicaments[idx]
    if element[1] != 0:
        print(f"{element[0]} - {element[1]}")

if textiles:
    print(f"Textiles left: {', '.join([str(el) for el in textiles])}")
if medicaments:
    medicaments = reversed(medicaments)
    print(f"Medicaments left: {', '.join([str(el) for el in medicaments])}")
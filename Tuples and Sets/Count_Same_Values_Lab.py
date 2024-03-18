numbers = [float(x) for x in input().split()]

dic_occ = {}
for num in numbers:
    if num not in dic_occ:
        dic_occ[num] = 1
    else:
        dic_occ[num] += 1

for key, value in dic_occ.items():
    print(f"{key} - {value} times")
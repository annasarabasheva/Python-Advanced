import itertools

n = int(input())
chemicals = []
for _ in range(n):
    chemical_el = input().split()
    chemicals.append(chemical_el)

merged = list(itertools.chain(*chemicals))
new_set = set()
for el in merged:
    new_set.add(el)

for i in new_set:
    print(i)
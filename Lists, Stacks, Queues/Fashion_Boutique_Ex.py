numbers = [int(x) for x in input().split()]
capacity = int(input())

racks = 1
sum_capacity = capacity
while numbers:
    removed_clothes = numbers.pop()
    if removed_clothes <= sum_capacity:
        sum_capacity -= removed_clothes
    else:
        racks += 1
        sum_capacity = capacity - removed_clothes

print(racks)

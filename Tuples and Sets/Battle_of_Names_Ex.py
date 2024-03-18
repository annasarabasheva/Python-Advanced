n = int(input())
even_set = set()
odd_set = set()
for i in range(n):
    name = input()
    sum_numbers = 0
    for el in name:
        sum_numbers += ord(el)
    new_sum = sum_numbers // (i + 1)
    if new_sum % 2 == 0:
        even_set.add(new_sum)
    else:
        odd_set.add(new_sum)

sum_even = sum(even_set)
sum_odd = sum(odd_set)
if sum_even == sum_odd:
    print(*odd_set.union(even_set), sep=", ")
elif sum_odd > sum_even:
    print(*odd_set.difference(even_set), sep=", ")
elif sum_odd < sum_even:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
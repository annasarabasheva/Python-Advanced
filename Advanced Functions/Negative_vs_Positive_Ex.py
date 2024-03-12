numbers = [int(el) for el in input().split()]
sum_positive = 0
sum_negative = 0
for num in numbers:
    if num < 0:
        sum_negative += num
    else:
        sum_positive += num

print(sum_negative)
print(sum_positive)
if abs(sum_negative) > sum_positive:
    print("The negatives are stronger than the positives")
elif abs(sum_negative) < sum_positive:
    print("The positives are stronger than the negatives")
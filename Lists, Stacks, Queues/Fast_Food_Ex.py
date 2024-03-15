from collections import deque

quantity_food = int(input())
orders = deque([int(x) for x in input().split()])
print(max(orders))

for el in orders.copy():
    if el <= quantity_food:
        quantity_food -= el
        orders.popleft()
    else:
        break

if orders:
    new_orders = [str(x) for x in orders]
    print(f"Orders left: {' '.join(new_orders)}")
else:
    print("Orders complete")
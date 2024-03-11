from collections import deque

orders = deque([int(el) for el in input().split(', ')])
capacities = deque([int(el) for el in input().split(', ')])
total_pizza = 0
while orders and capacities:
    order = orders.popleft()
    capacity = capacities.pop()
    left_pizza = 0
    if order > 10 or order <= 0:
        capacities.append(capacity)
        continue

    if order <= capacity:
        total_pizza += order
        continue
    elif capacity < order:
        left_pizza = order - capacity
        orders.appendleft(left_pizza)
        total_pizza += capacity

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}\nEmployees: {', '.join([str(el) for el in capacities])}")
else:
    print(f"Not all orders are completed.\nOrders left: {', '.join([str(el) for el in orders])}")
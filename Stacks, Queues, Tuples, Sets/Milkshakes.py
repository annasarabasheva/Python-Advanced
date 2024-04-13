from collections import deque
chocolate = deque([int(el) for el in input().split(', ')])
cups_milk = deque([int(el) for el in input().split(', ')])
milkshake = 0
while milkshake != 5 and chocolate and cups_milk:
    choco = chocolate.pop()
    milk = cups_milk.popleft()
    if choco <= 0 and milk <= 0:
        continue
    elif choco <= 0:
        cups_milk.appendleft(milk)
        continue
    elif milk <= 0:
        chocolate.append(choco)
        continue
    if choco == milk:
        milkshake += 1
    else:
        cups_milk.append(milk)
        chocolate.append(choco - 5)

if milkshake < 5:
    print("Not enough milkshakes.")
else:
    print("Great! You made all the chocolate milkshakes needed!")

if chocolate:
    print(f"Chocolate: {', '.join(str(el) for el in chocolate)}")
else:
    print("Chocolate: empty")

if cups_milk:
    print(f"Milk: {', '.join(str(el) for el in cups_milk)}")
else:
    print(f"Milk: empty")







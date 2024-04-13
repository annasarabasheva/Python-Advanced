from collections import deque
working_bees = deque([int(el) for el in input().split()])
nectar = deque([int(el) for el in input().split()])
symbols = deque(input().split())
sum_honey = 0

#bees 30
#honey 20
while working_bees and nectar:
    bee = working_bees.popleft()
    honey = nectar.pop()
    if bee > honey:
        working_bees.appendleft(bee)
    elif bee <= honey:
        symbol = symbols.popleft()
        if symbol == "+":
            result = abs(bee + honey)
            sum_honey += result
        elif symbol == "-":
            result = abs(bee - honey)
            sum_honey += result
        elif symbol == "*":
            result = abs(bee * honey)
            sum_honey += result
        elif symbol == "/":
            if honey == 0:
                continue
            result = abs(bee / honey)
            sum_honey += result

print(f"Total honey made: {sum_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(el) for el in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(el) for el in nectar)}")
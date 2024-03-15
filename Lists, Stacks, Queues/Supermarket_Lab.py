from collections import deque

people_deque = deque()

while True:
    name = input()
    if name == "Paid":
        for el in people_deque:
            print(el)

        people_deque.clear()
        continue
    if name == "End":
        print(f"{len(people_deque)} people remaining.")
        break

    people_deque.append(name)


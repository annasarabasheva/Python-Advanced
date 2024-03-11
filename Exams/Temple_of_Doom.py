from collections import deque

tools = deque([int(el) for el in input().split()])
substances = deque([int(el) for el in input().split()])
challenges = [int(el) for el in input().split()]

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()
    multiplication = tool * substance
    if multiplication in challenges:
        challenges.remove(multiplication)

    else:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance == 0:
            substances.append(substance)
            substances.pop()

        else:
            substances.append(substance)
    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break


if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join([str(el) for el in tools])}")
if substances:
    print(f"Substances: {', '.join([str(el) for el in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(el) for el in challenges])}")

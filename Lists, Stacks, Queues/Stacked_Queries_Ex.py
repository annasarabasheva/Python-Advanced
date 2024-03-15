from collections import deque
stack = deque()
n = int(input())
for i in range(n):
    query = [int(x) for x in input().split()]
    command = query[0]
    if command == 1:
        stack.append(query[1])
    elif command == 2:
        if stack:
            stack.pop()
    elif command == 3:
        if stack:
            print(max(stack))
    elif command == 4:
        if stack:
            print(min(stack))
stack.reverse()
new_stack = []
for el in stack:
    new_el = str(el)
    new_stack.append(new_el)

print(', '.join(new_stack))
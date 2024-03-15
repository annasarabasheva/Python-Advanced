from collections import deque

par = deque(input())

open_par = deque()
while par:
    current_par = par.popleft()
    if current_par in "[{(":
        open_par.append(current_par)
    elif not open_par:
        print("NO")
        break
    else:
        if f"{open_par.pop() + current_par}" not in "[]{}()":
            print("NO")
            break

else:
    print("YES")
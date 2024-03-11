from collections import deque

egg_sizes = deque([int(el) for el in input().split(", ")])
paper_sizes = deque([int(el) for el in input().split(", ")])
boxes = 0
while egg_sizes and paper_sizes:
    egg = egg_sizes.popleft()
    paper = paper_sizes.pop()
    if egg <= 0:
        paper_sizes.append(paper)
        continue
    if egg == 13:
        paper_first_pos = paper_sizes.popleft()
        paper_sizes.appendleft(paper)
        paper_sizes.append(paper_first_pos)
        continue
    wrapped = egg + paper
    if wrapped <= 50:
        boxes += 1

if boxes >= 1:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_sizes:
    print(f"Eggs left: {', '.join([str(el) for el in egg_sizes])}")
if paper_sizes:
    print(f"Pieces of paper left: {', '.join([str(el) for el in paper_sizes])}")
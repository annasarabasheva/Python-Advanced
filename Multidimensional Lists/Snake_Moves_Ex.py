from collections import deque
rows, cols = [int(el) for el in input().split()]
word = list(input())
word_copy = deque(word.copy())

for r in range(rows):
    while len(word_copy) < cols:
        word_copy.extend(word)

    if r % 2 == 0:
        print(*[word_copy.popleft() for c in range(cols)], sep="")
    else:
        print(*[word_copy.popleft() for c in range(cols)][::-1], sep="")
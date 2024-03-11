from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())
found_word = False
flowers = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

while vowels and consonants:
    v = vowels.popleft()
    c = consonants.pop()
    for key, value in flowers.items():
        if v in key:
            flowers[key] = flowers[key].replace(v, "")
            if flowers[key] == "":
                found_word = True
                break
        if c in key:
            flowers[key] = flowers[key].replace(c, "")
            if flowers[key] == "":
                found_word = True
                break
    if found_word:
        break

if found_word:
    word = []
    for key, value in flowers.items():
        if value == "":
            word.append(key)

    print(f"Word found: {''.join(word)}")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
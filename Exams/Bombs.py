from collections import deque

effects = deque([int(el) for el in input().split(', ')])
casings = deque([int(el) for el in input().split(', ')])
bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
bombs_collected = False
while effects and casings:
    effect = effects.popleft()
    casing = casings.pop()
    combination = effect + casing
    if combination == 40:
        bombs["Datura Bombs"] += 1
    elif combination == 60:
        bombs["Cherry Bombs"] += 1
    elif combination == 120:
        bombs["Smoke Decoy Bombs"] += 1
    else:
        casing -= 5
        casings.append(casing)
        effects.appendleft(effect)

    if bombs["Datura Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3:
        bombs_collected = True
        break

if bombs_collected:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if effects:
    print(f"Bomb Effects: {', '.join([str(el) for el in effects])}")
else:
    print("Bomb Effects: empty")
if casings:
    print(f"Bomb Casings: {', '.join([str(el) for el in casings])}")
else:
    print("Bomb Casings: empty")

for key, value in sorted(bombs.items()):
    print(f"{key}: {value}")
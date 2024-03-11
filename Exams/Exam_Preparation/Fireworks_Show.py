from collections import deque

firework_effects = deque([int(el) for el in input().split(", ")])
explosive_power = deque([int(el) for el in input().split(", ")])
palm_firework = 0
willow_firework = 0
crossette_firework = 0
enough_fireworks = False
while firework_effects and explosive_power:
    firework = firework_effects.popleft()
    power = explosive_power.pop()
    if firework <= 0 and power <= 0:
        continue
    elif firework <= 0 and power > 0:
        explosive_power.append(power)
        continue
    elif power <= 0 and firework > 0:
        firework_effects.appendleft(firework)
        continue

    combination = firework + power

    if combination % 3 == 0 and combination % 5 != 0:
        palm_firework += 1
    elif combination % 5 == 0 and combination % 3 != 0:
        willow_firework += 1
    elif combination % 3 == 0 and combination % 5 == 0:
        crossette_firework += 1
    else:
        firework -= 1
        firework_effects.append(firework)
        explosive_power.append(power)

    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        enough_fireworks = True
        print("Congrats! You made the perfect firework show!")
        break


if not enough_fireworks:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join([str(el) for el in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")
print(f"Palm Fireworks: {palm_firework}\nWillow Fireworks: {willow_firework}\nCrossette Fireworks: {crossette_firework}")



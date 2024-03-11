def flights(*args):
    passengers = {}
    for idx in range(len(args) - 1):
        el = args[idx]
        if isinstance(el, str) and el != "Finish":
            if el not in passengers:
                passengers[el] = 0
            passengers[el] += int(args[idx + 1])
        elif el == "Finish":
            break
    return passengers


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
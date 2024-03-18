n = int(input())
set_guests = set()
for i in range(n):
    reservation = input()
    set_guests.add(reservation)

while True:
    guests = input()
    if guests == "END":
        break
    if guests in set_guests:
        set_guests.remove(guests)

print(len(set_guests))
for guest in sorted(set_guests):
    print(guest)

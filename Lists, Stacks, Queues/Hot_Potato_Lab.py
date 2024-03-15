from collections import deque

players = deque(input().split())
toss = int(input()) - 1
while len(players) > 1:
    players.rotate(-toss)
    exited_name = players.popleft()
    print(f"Removed {exited_name}")


print(f"Last is {players.popleft()}")
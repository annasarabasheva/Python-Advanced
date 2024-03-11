from collections import deque

times = deque([int(el) for el in input().split()])
tasks = deque([int(el) for el in input().split()])

darth_vader = 0
thor = 0
blue = 0
yellow = 0
while times and tasks:
    time = times.popleft()
    task = tasks.pop()
    multiplication = time * task
    if 0 <= multiplication <= 60:
        darth_vader += 1
    elif 61 <= multiplication <= 120:
        thor += 1
    elif 121 <= multiplication <= 180:
        blue += 1
    elif 181 <= multiplication <= 240:
        yellow += 1
    else:
        task -= 2
        tasks.append(task)
        times.append(time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {darth_vader}\nThor Ducky: {thor}\nBig Blue Rubber Ducky: {blue}\nSmall Yellow Rubber Ducky: {yellow}")
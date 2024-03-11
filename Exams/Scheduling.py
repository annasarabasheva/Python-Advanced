jobs = [int(el) for el in input().split(', ')]
index = int(input())
jobs_copy = jobs.copy()
cycles = 0
index_found = False
while jobs:
    for el in jobs_copy:
        least_work = min(jobs)
        if jobs_copy.count(least_work) == 1:
            index_min = jobs_copy.index(least_work)
            if index_min != index:
                cycles += least_work
                jobs.remove(least_work)
            elif index_min == index:
                cycles += least_work
                index_found = True
                break
        elif jobs_copy.count(least_work) > 1:
            index_min = jobs_copy.index(least_work)
            jobs_copy[index_min] = 0
            if index_min != index:
                cycles += least_work
                jobs.remove(least_work)
            elif index_min == index:
                cycles += least_work
                index_found = True
                break
    if index_found:
        break

print(cycles)
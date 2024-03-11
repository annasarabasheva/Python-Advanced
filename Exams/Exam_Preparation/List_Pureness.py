from collections import deque


def best_list_pureness(list, K):
    list = deque(list)
    dic = {}
    rotation = 0
    pureness = 0
    for idx in range(len(list)):
        el = list[idx]
        pureness += el * idx
        dic[rotation] = pureness
    for i in range(K):
        rotation += 1
        list.rotate()
        pureness = 0
        for idx in range(len(list)):
            element = list[idx]
            pureness += element * idx

        dic[rotation] = pureness

    all_values = []
    for value in dic.values():
        all_values.append(value)
    max_num = max(all_values)
    rotation_num = []
    for key, value in dic.items():
        if value == max_num and value not in rotation_num:
            rotation_num.append(key)
    return f"Best pureness {max_num} after {rotation_num[0]} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

def sorting_cheeses(**kwargs):
    res = ''
    sorted_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for i in range(len(sorted_cheese)):
        res += sorted_cheese[i][0] + "\n"
        sorted_cheese[i][1].sort(reverse=True)
        for el in sorted_cheese[i][1]:
            res += str(el) + "\n"
    return res



print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125],))
print(sorting_cheeses(Parmigiano=[165, 215], Feta=[150, 515], Brie=[150, 125] ))
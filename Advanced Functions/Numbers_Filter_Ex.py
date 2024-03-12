def even_odd_filter(**kwargs):
    even = []
    odd = []
    for key, value in kwargs.items():
        if key == "even":
            for num in value:
                if num % 2 == 0:
                    even.append(num)
        elif key == "odd":
            for num in value:
                if num % 2 != 0:
                    odd.append(num)
    for key, value in kwargs.items():
        if key == "even":
            value.clear()
            value.extend(even)
        elif key == "odd":
            value.clear()
            value.extend(odd)
    kwargs = sorted(kwargs.items(), key=lambda x: -len(x[1]))
    dic ={}
    for i in range(len(kwargs)):
        dic[kwargs[i][0]] = kwargs[i][1]
    return dic



print(even_odd_filter(
        odd=[1, 2, 3, 4, 10, 5],
        even=[3, 4, 5, 7, 10, 2, 5, 5, 2],)
)

print(even_odd_filter(
odd=[2, 2, 30, 44, 10, 5],
))
def words_sorting(*args):
    dic = {}
    sum_values = 0
    for arg in args:
        result = 0
        for el in arg:
            result += ord(el)
        dic[arg] = result
        sum_values += result

    if sum_values % 2 != 0:
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    else:
        dic = sorted(dic.items(), key=lambda x: x[0])

    final_result = ""
    for i in range(len(dic)):
        final_result += f"{dic[i][0]} - {dic[i][1]}\n"

    return final_result


print(words_sorting('escape', 'charm', 'mythology'))
print(words_sorting('escape', 'charm', 'eye'))
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))

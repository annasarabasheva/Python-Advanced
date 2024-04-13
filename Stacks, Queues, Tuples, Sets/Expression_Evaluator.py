from math import floor
math_line = input().split()
numbers = []
for index in range(len(math_line)):
    element = math_line[index]
    if element not in "*/+-":
        numbers.append(int(element))
    elif element == "*":
        result = 1
        for n in numbers:
            result = result * n
        numbers.clear()
        numbers.append(result)
    elif element == "+":
        result = 0
        for n in numbers:
            result = result + n
        numbers.clear()
        numbers.append(result)
    elif element == "-":
        result = 0
        for idx in range(len(numbers)):
            if idx == 0:
                result = numbers[idx] - result
            else:
                result = result - numbers[idx]
        numbers.clear()
        numbers.append(result)
    elif element == "/":
        result = 1
        for idx in range(len(numbers)):
            if idx == 0:
                result = floor(numbers[idx] / result)
            else:
                result = floor(result / numbers[idx])
        numbers.clear()
        numbers.append(result)

print(*numbers)



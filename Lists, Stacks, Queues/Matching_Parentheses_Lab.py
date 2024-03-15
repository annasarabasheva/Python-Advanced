text = input()
stack = []
for index in range(len(text)):
    element = text[index]
    if element == "(":
        stack.append(index)

    elif element == ")":
        start_position = stack.pop()
        end_position = index
        print(text[start_position:end_position + 1])

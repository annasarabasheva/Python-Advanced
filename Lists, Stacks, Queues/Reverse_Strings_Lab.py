text = input()
stack = list(text)
for index in range(len(stack)):
    removed_element = stack.pop()
    print(removed_element, end="")


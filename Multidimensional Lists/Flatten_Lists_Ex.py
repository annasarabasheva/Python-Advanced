text = [int(el) if el.isdigit() else el for el in input().split('|')]
text = text[::-1]
new_text = " ".join(str(el) for el in text)
new_new = new_text.split()
print(*new_new)
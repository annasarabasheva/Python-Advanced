m, n = [int(el) for el in input().split()]
m_elements = set()
for i in range(m):
    number = int(input())
    m_elements.add(number)

n_elements = set()
for y in range(n):
    number_two = int(input())
    n_elements.add(number_two)

print(*m_elements.intersection(n_elements), sep="\n")
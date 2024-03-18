n = int(input())
dic_students = {}

for i in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name not in dic_students:
        dic_students[name] = []

    dic_students[name].append(grade)


for name, grade in dic_students.items():
    average = sum(grade) / len(grade)
    print(f"{name} -> {' '.join([str(f'{x:.2f}') for x in grade])} (avg: {average:.2f})")
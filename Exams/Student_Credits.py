def students_credits(*args):
    total_credit = 0
    dic_d = {}
    for idx in range(len(args)):
        element = args[idx]
        all_elements = element.split("-")
        name = all_elements[0]
        max_credits = int(all_elements[1])
        max_points = int(all_elements[2])
        d_points = int(all_elements[3])
        result = (d_points / max_points) * max_credits
        total_credit += result
        dic_d[name] = result

    dic_d = sorted(dic_d.items(), key=lambda x: (-x[1], x[0]))
    result = ""
    if total_credit >= 240:
        result += f"Diyan gets a diploma with {total_credit:.1f} credits.\n"
    else:
        result += f"Diyan needs {(240 - total_credit):.1f} credits more for a diploma.\n"
    for idx in range(len(dic_d)):
        element = dic_d[idx]
        name = element[0]
        credits = element[1]
        result += f"{name} - {credits:.1f}\n"

    return result


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)


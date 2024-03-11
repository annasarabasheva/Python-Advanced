def gather_credits(needed_credits, *args):
    courses = []
    gathered_credits = 0
    for idx in range(len(args)):
        element = args[idx]
        course_name = element[0]
        credits = element[1]
        if gathered_credits < needed_credits:
            if course_name not in courses:
                courses.append(course_name)
                gathered_credits += credits

            else:
                continue
        elif gathered_credits >= needed_credits:
            break

    if gathered_credits >= needed_credits:
        courses_sorted = sorted(courses)
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(courses_sorted)}"
    else:
        return f"You need to enroll in more courses! You have to gather {needed_credits - gathered_credits} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))
print()
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print()
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))


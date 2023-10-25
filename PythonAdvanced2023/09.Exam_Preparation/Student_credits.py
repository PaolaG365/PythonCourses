TARGET_CREDITS = 240


def students_credits(*info):
    total_credits = 0
    student_info = {}
    result = []
    for results_course in info:
        course_name, max_credits, max_test_points, student_points = (
            [int(x) if x.isdigit() else x for x in results_course.split("-")])
        received_credits = (student_points / max_test_points) * max_credits
        student_info[course_name] = received_credits
        total_credits += received_credits

    if total_credits >= TARGET_CREDITS:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {TARGET_CREDITS - total_credits:.1f} credits more for a diploma.")

    for course, credits_student in sorted(student_info.items(), key=lambda x: -x[1]):
        result.append(f"{course} - {credits_student:.1f}")

    return "\n".join(result)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490",
    )
)
print()
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
print()
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)

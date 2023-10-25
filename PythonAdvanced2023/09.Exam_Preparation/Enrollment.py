def gather_credits(credits_target: int, *courses_info):
    total_credits = 0
    enrolled_courses = {}
    result = []

    for course_name, course_credits in courses_info:
        if total_credits < credits_target:
            if course_name not in enrolled_courses:
                enrolled_courses[course_name] = course_credits
                total_credits += course_credits
        else:
            break

    if total_credits < credits_target:
        result.append(f"You need to enroll in more courses! "
                      f"You have to gather {credits_target - total_credits} credits more.")
    else:
        # if it's one single dot the problem .... it was
        result.append(f"Enrollment finished! Maximum credits: {total_credits}.")
        result.append(f"Courses: {', '.join([course for course in sorted(enrolled_courses)])}")

    return "\n".join(result)


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

courses_dict = {}
command = input()

while command != "end":
    course, student = command.split(" : ")

    if course not in courses_dict:
        courses_dict[course] = []
    courses_dict[course].append(student)

    command = input()

for course_name in courses_dict:
    print(f"{course_name}: {len(courses_dict[course_name])}")
    for student_name in courses_dict[course_name]:
        print(f"-- {student_name}")

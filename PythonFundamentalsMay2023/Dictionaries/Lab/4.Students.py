courses = {}

student = input()

while student not in courses.keys():
    student = student.split(":")
    name = student[0]
    id_student = int(student[1])
    course = student[2]

    if course in courses:
        courses[course].update({name: id_student})
    else:
        courses[course] = {name: id_student}

    student = input().replace("_", " ")  # last line for course searched, received in snake case

for learning_body in courses[student]:
    print(f"{learning_body} - {courses[student].get(learning_body)}")

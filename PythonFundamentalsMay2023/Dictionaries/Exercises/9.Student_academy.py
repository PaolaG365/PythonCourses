student_grades_lines = int(input())
acceptable_students = {}
AVERAGE_GRADE = 4.50

for line in range(student_grades_lines):
    student = input()
    grade = float(input())

    if student not in acceptable_students:
        acceptable_students[student] = grade
    else:
        acceptable_students[student] = (acceptable_students[student] + grade) / 2

    if acceptable_students[student] < AVERAGE_GRADE:
        del acceptable_students[student]

for student_name, student_grade in acceptable_students.items():
    print(f"{student_name} -> {student_grade:.2f}")

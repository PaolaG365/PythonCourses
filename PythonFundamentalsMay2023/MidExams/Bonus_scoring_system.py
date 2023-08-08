import math

number_of_students = int(input())
lectures_number = int(input())
additional_bonus = int(input())
max_bonus = 0
attendance_best_student = 0

for student in range(number_of_students):
    student_attendance = int(input())
    bonus_student = student_attendance / lectures_number * (5 + additional_bonus)
    if bonus_student > max_bonus:
        max_bonus = bonus_student
        attendance_best_student = student_attendance

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {attendance_best_student} lectures.")

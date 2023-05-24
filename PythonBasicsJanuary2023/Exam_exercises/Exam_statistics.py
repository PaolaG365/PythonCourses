number_students = int(input())

failed, good, very_good, excellent = 0, 0, 0, 0
total_grades = 0

for _ in range(number_students):
    grade_student = float(input())
    total_grades += grade_student

    if grade_student < 3.00:
        failed += 1
    elif 3.00 <= grade_student <= 3.99:
        good += 1
    elif 4.00 <= grade_student <= 4.99:
        very_good += 1
    else:
        excellent += 1

print(f"Top students: {excellent / number_students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {very_good / number_students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {good / number_students * 100:.2f}%")
print(f"Fail: {failed / number_students * 100:.2f}%")
print(f"Average: {total_grades / number_students:.2f}")

students_number = int(input())

top, very_good, good, failed = 0, 0, 0, 0
average_grade = 0

for _ in range(students_number):
    grade = float(input())
    if grade < 3.00:
        failed += 1
        average_grade += grade
    elif grade <= 3.99:
        good += 1
        average_grade += grade
    elif grade <= 4.99:
        very_good += 1
        average_grade += grade
    else:
        top += 1
        average_grade += grade

print(f'Top students: {top / students_number * 100:.2f}%')
print(f'Between 4.00 and 4.99: {very_good / students_number * 100:.2f}%')
print(f'Between 3.00 and 3.99: {good / students_number * 100:.2f}%')
print(f'Fail: {failed / students_number * 100:.2f}%')
print(f'Average: {average_grade / students_number:.2f}')

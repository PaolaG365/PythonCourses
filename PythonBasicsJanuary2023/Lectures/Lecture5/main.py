name_student = input()

grade = 1
failed = 0
total_score = 0

while grade <= 12:
    grade_for_the_year = float(input())

    if grade_for_the_year < 4.00:
        failed += 1
        if failed == 2:
            print(f'{name_student} has been excluded at {grade} grade')
            break
    else:
        total_score += grade_for_the_year
        grade += 1

else:
    print(f'{name_student} graduated. Average grade: {total_score / 12:.2f}')

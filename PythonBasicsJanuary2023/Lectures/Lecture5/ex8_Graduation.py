name_student = input()

grade = 1
failed = 0
total_score = 0

for grade in range(1, 13):
    if failed == 2:
        print(f'{name_student} has been excluded at {grade} grade')
        break
    else:
        grade_for_the_year = float(input())
        total_score += grade_for_the_year
    if grade_for_the_year < 4.00:
        failed += 1

else:
    print(f'{name_student} graduated. Average grade: {total_score / grade:.2f}')

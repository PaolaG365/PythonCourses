student_name = input()
grades = 0
counter = 0
tries = 2

while counter < 12:
    grade = float(input())

    if grade < 4:
        tries -= 1
        if tries == 0:
            break
    else:
        grades += grade
        counter += 1

if counter < 12:
    print(f"{student_name} has been excluded at {counter + 1} grade")
else:
    print(f"{student_name} graduated. Average grade: {grades / 12:.2f}")

jury_number = int(input())

presentation_count = 0
total_grade = 0

while True:
    presentation = input()

    if presentation == "Finish":
        break

    presentation_count += 1
    grade_sum = 0

    for _ in range(jury_number):
        grade = float(input())
        grade_sum += grade

    print(f'{presentation} - {grade_sum / jury_number:.2f}.')

    total_grade += grade_sum

print(f"Student's final assessment is {total_grade / (presentation_count * jury_number):.2f}.")

failed_grades_allowed = int(input())

last_test_name = ''
count_f = 0
total_grade = 0
test_count = 0

while True:
    test_name = input()

    if test_name == "Enough":
        print(f'Average score: {total_grade / test_count:.2f}\n'
              f'Number of problems: {test_count}\nLast problem: {last_test_name}')
        break

    grade = int(input())
    total_grade += grade
    last_test_name = test_name
    test_count += 1

    if grade <= 4.00:
        count_f += 1
    if count_f == failed_grades_allowed:
        print(f"You need a break, {count_f} poor grades.")
        break

number_grades = int(input())
students_book = {}

for _ in range(number_grades):
    name, grade = input().split()
    if name not in students_book:
        students_book[name] = []
    students_book[name].append(float(grade))

for student, grades in students_book.items():
    print(f"{student} -> {' '.join([f'{el:.2f}' for el in grades])} "
          f"(avg: {sum(grades)/len(grades):.2f})")

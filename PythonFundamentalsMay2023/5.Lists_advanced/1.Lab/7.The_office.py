employees_happiness = [int(n) for n in input().split()]
happiness_factor = int(input())

employees_happiness = [x * happiness_factor for x in employees_happiness]
average_employees_happiness = sum(employees_happiness) / len(employees_happiness)
happy_count = [e for e in employees_happiness if e >= average_employees_happiness]

if len(happy_count) >= int(len(employees_happiness) / 2):
    print(f"Score: {len(happy_count)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_count)}/{len(employees_happiness)}. Employees are not happy!")

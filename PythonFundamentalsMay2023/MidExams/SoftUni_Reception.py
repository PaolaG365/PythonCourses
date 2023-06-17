first_receptionist_efficiency = int(input())
second_receptionist_efficiency = int(input())
third_receptionist_efficiency = int(input())
students_count = int(input())

per_hour_students = first_receptionist_efficiency + second_receptionist_efficiency + third_receptionist_efficiency
hours = 0

while students_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students_count -= per_hour_students

print(f"Time needed: {hours}h.")

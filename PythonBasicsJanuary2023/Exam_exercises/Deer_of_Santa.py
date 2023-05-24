import math

days, food_in_kg = int(input()), int(input())
first_deer, second_deer, third_deer = float(input()), float(input()), float(input())

first_total = days * first_deer
second_total = days * second_deer
third_total = days * third_deer
total_needed = first_total + second_total + third_total

if total_needed <= food_in_kg:
    print(f"{math.floor(food_in_kg - total_needed)} kilos of food left.")
else:
    print(f"{math.ceil(total_needed - food_in_kg)} more kilos of food are needed.")

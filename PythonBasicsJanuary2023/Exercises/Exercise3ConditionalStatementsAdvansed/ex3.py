flower_type = input()
number_flowers, budget = int(input()), int(input())

total = 0

if flower_type == "Roses":
    total = number_flowers * 5
    if number_flowers > 80:
        total -= (total * 0.1)

if flower_type == "Dahlias":
    total = number_flowers * 3.80
    if number_flowers > 90:
        total -= (total * 0.15)

if flower_type == "Tulips":
    total = number_flowers * 2.80
    if number_flowers > 80:
        total -= (total * 0.15)

if flower_type == "Narcissus":
    total = number_flowers * 3
    if number_flowers < 120:
        total += (total * 0.15)

if flower_type == "Gladiolus":
    total = number_flowers * 2.50
    if number_flowers < 80:
        total += (total * 0.2)

if total <= budget:
    print(f'Hey, you have a great garden with {number_flowers}'
          f' {flower_type} and {budget - total:.2f} leva left.')
else:
    print(f"Not enough money, you need {total - budget:.2f} leva more.")

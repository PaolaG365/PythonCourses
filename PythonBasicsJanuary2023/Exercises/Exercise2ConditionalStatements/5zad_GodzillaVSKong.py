budget = float(input())
extras = int(input())
outfit_price = float(input())

film_set = budget * 0.1
fits_total = extras * outfit_price

if extras > 150:
    fits_total -= fits_total * 0.1

total_cost = film_set + fits_total

if total_cost <= budget:
    a = budget - total_cost
    print(f'Action! \nWingard starts filming with {a:.2f} leva left.')
else:
    a = total_cost - budget
    print(f'Not enough money!\nWingard needs {a:.2f} leva more.')

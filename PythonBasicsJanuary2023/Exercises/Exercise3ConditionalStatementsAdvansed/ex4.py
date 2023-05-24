budget = int(input())
season = input()
number_fishermen = int(input())

total = 0

if season == "Spring":
    if number_fishermen <= 6:
        total = 3000 - (3000 * 0.1)
    elif 7 < number_fishermen <= 11:
        total = 3000 - (3000 * 0.15)
    else:
        total = 3000 - (3000 * 0.25)

if season == "Summer" or season == "Autumn":
    if number_fishermen <= 6:
        total = 4200 - (4200 * 0.1)
    elif 7 < number_fishermen <= 11:
        total = 4200 - (4200 * 0.15)
    else:
        total = 4200 - (4200 * 0.25)

if season == "Winter":
    if number_fishermen <= 6:
        total = 2600 - (2600 * 0.1)
    elif 7 < number_fishermen <= 11:
        total = 2600 - (2600 * 0.15)
    else:
        total = 2600 - (2600 * 0.25)

if number_fishermen % 2 == 0 and season != "Autumn":
    total -= total * 0.05

if budget >= total:
    print(f'Yes! You have {budget - total:.2f} leva left.')
else:
    print(f'Not enough money! You need {total - budget:.2f} leva.')

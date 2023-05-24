budget = float(input())
season = input()

destination, type_vacation = None, None
price_vacation = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == "summer":
        price_vacation = budget * 0.30
        type_vacation = 'Camp'
    elif season == "winter":
        price_vacation = budget * 0.70
        type_vacation = 'Hotel'

if 100 < budget <= 1000:
    destination = 'Balkans'
    if season == "summer":
        price_vacation = budget * 0.40
        type_vacation = 'Camp'
    elif season == "winter":
        price_vacation = budget * 0.80
        type_vacation = 'Hotel'

if budget > 1000:
    destination = "Europe"
    price_vacation = budget * 0.90
    type_vacation = "Hotel"

print(f'Somewhere in {destination}\n{type_vacation} - {price_vacation:.2f}')

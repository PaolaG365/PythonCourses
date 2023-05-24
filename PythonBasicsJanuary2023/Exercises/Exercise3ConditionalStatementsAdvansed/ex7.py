month = input()
number_nights = int(input())

studio_price, apartment_price = 0, 0

if month == "May" or month == "October":
    studio_price = number_nights * 50
    apartment_price = number_nights * 65
    if 7 < number_nights <= 14:
        studio_price -= studio_price * 0.05
    elif number_nights > 14:
        studio_price -= studio_price * 0.3

elif month == "June" or month == "September":
    studio_price = number_nights * 75.20
    apartment_price = number_nights * 68.70
    if number_nights > 14:
        studio_price -= studio_price * 0.2

elif month == "July" or month == "August":
    studio_price = number_nights * 76
    apartment_price = number_nights * 77

if number_nights > 14:
    apartment_price -= apartment_price * 0.1

print(f'Apartment: {apartment_price:.2f} lv.\nStudio: {studio_price:.2f} lv.')

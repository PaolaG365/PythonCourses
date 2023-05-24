season, group_type = input(), input()
students_number, nights_staying = int(input()), int(input())

price_for_one_night = 0
sport = ""

if season == "Winter":
    if group_type == "girls":
        sport = "Gymnastics"
        price_for_one_night = 9.60
    elif group_type == "boys":
        sport = "Judo"
        price_for_one_night = 9.60
    elif group_type == "mixed":
        sport = "Ski"
        price_for_one_night = 10

elif season == "Spring":
    if group_type == "girls":
        sport = "Athletics"
        price_for_one_night = 7.20
    elif group_type == "boys":
        sport = "Tennis"
        price_for_one_night = 7.20
    elif group_type == "mixed":
        sport = "Cycling"
        price_for_one_night = 9.50

elif season == "Summer":
    if group_type == "girls":
        sport = "Volleyball"
        price_for_one_night = 15
    elif group_type == "boys":
        sport = "Football"
        price_for_one_night = 15
    elif group_type == "mixed":
        sport = "Swimming"
        price_for_one_night = 20

total = nights_staying * price_for_one_night * students_number

if students_number >= 50:
    total -= total * 0.5
elif 20 <= students_number < 50:
    total -= total * 0.15
elif 10 <= students_number < 20:
    total -= total * 0.05

print(f'{sport} {total:.2f} lv.')

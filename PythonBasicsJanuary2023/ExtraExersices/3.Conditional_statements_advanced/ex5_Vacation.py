budget = float(input())
season = input()

location, accommodation_type = "", ""
price = 0

if budget <= 1000:
    accommodation_type = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    else:
        location = "Morocco"
        price = budget * 0.45

elif budget > 3000:
    accommodation_type = "Hotel"
    price = budget * 0.9
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"

else:
    accommodation_type = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.8
    else:
        location = "Morocco"
        price = budget * 0.6

print(f'{location} - {accommodation_type} - {price:.2f}')

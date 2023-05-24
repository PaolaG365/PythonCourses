days_staying = int(input())
room_type, rating = input(), input()

total = 0

if room_type == "room for one person":
    total = (days_staying - 1) * 18.00

elif room_type == "apartment":
    total = (days_staying - 1) * 25.00
    if days_staying < 10:
        total -= total * 0.3
    elif days_staying > 15:
        total -= total * 0.5
    else:
        total -= total * 0.35

elif room_type == "president apartment":
    total = (days_staying - 1) * 35.00
    if days_staying < 10:
        total -= total * 0.1
    elif days_staying > 15:
        total -= total * 0.2
    else:
        total -= total * 0.15

if rating == "positive":
    total += total * 0.25
elif rating == "negative":
    total -= total * 0.1

print(f'{total:.2f}')

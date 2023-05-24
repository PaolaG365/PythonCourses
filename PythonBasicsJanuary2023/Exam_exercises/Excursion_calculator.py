number_people = int(input())
season = input()

tax = 0

if number_people <= 5:
    if season == "spring":
        tax = 50.00
    elif season == "summer":
        tax = 48.50
    elif season == "autumn":
        tax = 60.00
    elif season == "winter":
        tax = 86.00
else:
    if season == "spring":
        tax = 48.00
    elif season == "summer":
        tax = 45.00
    elif season == "autumn":
        tax = 49.50
    elif season == "winter":
        tax = 85.00

total = number_people * tax

if season == "summer":
    total *= 0.85
elif season == "winter":
    total *= 1.08

print(f"{total:.2f} leva.")

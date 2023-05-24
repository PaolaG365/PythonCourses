chrysanthemums_number, roses_number, tulips_number = int(input()), int(input()), int(input())
season, holiday = input(), input()

total = 0

if season == "Spring" or season == "Summer":
    total = chrysanthemums_number * 2.00 + roses_number * 4.10 + tulips_number * 2.50
elif season == "Autumn" or season == "Winter":
    total = chrysanthemums_number * 3.75 + roses_number * 4.50 + tulips_number * 4.15

if holiday == "Y":
    total += total * 0.15

if tulips_number > 7 and season == "Spring":
    total -= total * 0.05

if roses_number >= 10 and season == "Winter":
    total -= total * 0.1

if (chrysanthemums_number + roses_number + tulips_number) > 20:
    total -= total * 0.2

print(f"{total + 2:.2f}")

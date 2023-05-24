season = input()
km_monthly = float(input())

salary = 0
per_km = 0

if km_monthly <= 5000:
    if season == "Spring" or season == "Autumn":
        per_km = 0.75
    elif season == "Summer":
        per_km = 0.90
    elif season == "Winter":
        per_km = 1.05

elif 5000 < km_monthly <= 10000:
    if season == "Spring" or season == "Autumn":
        per_km = 0.95
    elif season == "Summer":
        per_km = 1.10
    elif season == "Winter":
        per_km = 1.25

elif 10000 < km_monthly <= 20000:
    per_km = 1.45

salary = (km_monthly * per_km) * 4
print(f"{salary * .9:.2f}")

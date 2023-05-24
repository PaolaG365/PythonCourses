distance_traveled = int(input())
time_period = input()

price = 0

if distance_traveled >= 100:
    price = distance_traveled * 0.06

if 100 > distance_traveled >= 20:
    price = distance_traveled * 0.09

if distance_traveled < 20:
    if time_period == "day":
        price = distance_traveled * 0.79 + 0.70
    if time_period == 'night':
        price = distance_traveled * 0.90 + 0.70

print(f"{price:.2f}")

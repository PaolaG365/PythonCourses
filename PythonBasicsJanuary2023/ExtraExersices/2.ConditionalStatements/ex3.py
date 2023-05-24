import math

square_meters_vineyard = int(input())
grape_per_sqm = float(input())
wine_needed = int(input())
workers = int(input())

produced_wine = ((square_meters_vineyard * grape_per_sqm) * 0.4) / 2.5

if wine_needed > produced_wine:
    a = wine_needed - produced_wine
    a = math.floor(a)
    print(f'It will be a tough winter! More {a} liters wine needed.')

if produced_wine >= wine_needed:
    produced_wine = math.floor(produced_wine)
    print(f'Good harvest this year! Total wine: {produced_wine} liters.')
    a = produced_wine - wine_needed
    a = math.ceil(a)
    b = (produced_wine - wine_needed) / workers
    b = math.ceil(b)
    print(f'{a} liters left -> {b} liters per person.')

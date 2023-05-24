fuel_type = input()
liters_fuel = float(input())
club_card = input()

GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33
GAS_PRICE = 0.93

total = 0

if fuel_type == 'Gasoline':
    total = liters_fuel * GASOLINE_PRICE
    if club_card == 'Yes':
        total = liters_fuel * (GASOLINE_PRICE - 0.18)

if fuel_type == 'Diesel':
    total = liters_fuel * DIESEL_PRICE
    if club_card == 'Yes':
        total = liters_fuel * (DIESEL_PRICE - 0.12)

if fuel_type == 'Gas':
    total = liters_fuel * GAS_PRICE
    if club_card == 'Yes':
        total = liters_fuel * (GAS_PRICE - 0.08)

if 20 < liters_fuel <= 25:
    total -= (total * 0.08)

if liters_fuel > 25:
    total -= (total * 0.1)

print(f'{total:.2f} lv.')

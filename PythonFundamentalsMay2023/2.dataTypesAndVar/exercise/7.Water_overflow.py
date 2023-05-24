pouring_count = int(input())
tank_capacity = 255
poured_water = 0

for i in range(pouring_count):
    liters_poured = int(input())
    poured_water += liters_poured

    if poured_water > tank_capacity:
        poured_water -= liters_poured
        print("Insufficient capacity!")
        continue

print(poured_water)

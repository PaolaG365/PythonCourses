lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total = 0
broken_shield_counter = 0

for day in range(1, lost_fights + 1):
    if day % 2 == 0:
        total += helmet_price

    if day % 3 == 0:
        total += sword_price
        if day % 2 == 0:
            total += shield_price
            broken_shield_counter += 1
            if broken_shield_counter % 2 == 0:
                total += armor_price

print(f"Gladiator expenses: {total:.2f} aureus")

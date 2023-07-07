army_of_dragons = {}
number_dragons = int(input())

for dragon in range(number_dragons):
    colour, name, damage, health, armor = input().split()
    if colour not in army_of_dragons:
        army_of_dragons[colour] = {}

    damage = 45 if damage == "null" else int(damage)
    health = 250 if health == "null" else int(health)
    armor = 10 if armor == "null" else int(armor)

    if name not in army_of_dragons[colour]:
        army_of_dragons[colour][name] = {}
    army_of_dragons[colour][name] = {"damage": damage, "health": health, "armor": armor}


for type_dragon, dragon_stats in army_of_dragons.items():

    damage_total = 0
    health_total = 0
    armor_total = 0
    count_dragons = len(army_of_dragons[type_dragon])

    for dragon_name, dragon_stat in dragon_stats.items():
        damage_total += dragon_stats[dragon_name]['damage']
        health_total += dragon_stats[dragon_name]['health']
        armor_total += dragon_stats[dragon_name]['armor']

    print(f"{type_dragon}::({damage_total/count_dragons:.2f}/"
          f"{health_total/count_dragons:.2f}/"
          f"{armor_total/count_dragons:.2f})")

    for drake in sorted(dragon_stats):
        print(f"-{drake} -> damage: {dragon_stats[drake]['damage']},"
              f" health: {dragon_stats[drake]['health']},"
              f" armor: {dragon_stats[drake]['armor']}")

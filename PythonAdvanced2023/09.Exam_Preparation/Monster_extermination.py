from collections import deque

monsters_armor_value = deque([int(x) for x in input().split(",")])
soldier_attacks_value = deque([int(x) for x in input().split(",")])
total_killed_monsters = 0

while monsters_armor_value and soldier_attacks_value:
    monster_armor = monsters_armor_value.popleft()
    soldier_atk = soldier_attacks_value.pop()

    if soldier_atk >= monster_armor:
        soldier_atk -= monster_armor
        total_killed_monsters += 1
        if soldier_atk > 0:
            if soldier_attacks_value:
                soldier_attacks_value[-1] += soldier_atk
            else:
                soldier_attacks_value.append(soldier_atk)

    else:
        monster_armor -= soldier_atk
        monsters_armor_value.append(monster_armor)

if not monsters_armor_value:
    print("All monsters have been killed!")

if not soldier_attacks_value:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {total_killed_monsters}")

def potion(hp, pot):
    if hp + pot > 100:
        healing_amount = 100 - hp
    else:
        healing_amount = pot
    hp += healing_amount
    print(f"You healed for {healing_amount} hp.")
    print(f"Current health: {hp} hp.")
    return hp


def chest(coins, treasure):
    if treasure > 0:
        coins += treasure
    print(f"You found {treasure} bitcoins.")
    return coins


def fight(hp, monster_name, monster_damage, room):
    if hp - monster_damage <= 0:
        print(f"You died! Killed by {monster_name}.\nBest room: {room + 1}")
        exit()
    hp -= monster_damage
    print(f"You slayed {monster_name}.")
    return hp


health = 100
bitcoins = 0
levels = input().split("|")

for level in range(len(levels)):
    event = levels[level].split()
    command, number = event[0], int(event[1])

    if command == "potion":
        health = potion(health, number)
    elif command == "chest":
        bitcoins = chest(bitcoins, number)
    else:
        health = fight(health, command, number, level)
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}\nHealth: {health}")

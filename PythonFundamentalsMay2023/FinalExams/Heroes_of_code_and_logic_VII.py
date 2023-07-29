def cast_spell(dictionary, name, mana_needed, name_spell):
    if dictionary[name]["MP"] < mana_needed:
        print(f"{name} does not have enough MP to cast {name_spell}!")
    else:
        dictionary[name]["MP"] -= mana_needed
        print(f"{name} has successfully cast {name_spell}"
              f" and now has {dictionary[name]['MP']} MP!")
    return dictionary


def take_damage(dictionary, name, damage, attacked_by):
    if dictionary[name]["HP"] - damage <= 0:
        print(f"{name} has been killed by {attacked_by}!")
        del dictionary[name]
    else:
        dictionary[name]["HP"] -= damage
        print(f"{name} was hit for {damage} HP by {attacked_by} and "
              f"now has {dictionary[name]['HP']} HP left!")
    return dictionary


def recharge(dictionary, name, amount):
    if dictionary[name]["MP"] + amount > 200:
        amount_recharged = 200 - dictionary[name]["MP"]
    else:
        amount_recharged = amount
    dictionary[name]["MP"] += amount_recharged
    print(f"{name} recharged for {amount_recharged} MP!")
    return dictionary


def heal(dictionary, name, amount):
    if dictionary[name]["HP"] + amount > 100:
        amount_recharged = 100 - dictionary[name]["HP"]
    else:
        amount_recharged = amount
    dictionary[name]["HP"] += amount_recharged
    print(f"{name} healed for {amount_recharged} HP!")
    return dictionary


number_heroes = int(input())

heroes_info = {}

for _ in range(number_heroes):
    hero_stats = input().split()
    hero_name, health, mana = hero_stats[0], int(hero_stats[1]), int(hero_stats[2])
    if health > 100:
        health = 100
    if mana > 200:
        mana = 200
    if hero_name not in heroes_info:
        heroes_info[hero_name] = {}
    heroes_info[hero_name] = {'HP': health, "MP": mana}

command = input()

while command != "End":
    command = command.split(" - ")
    action, name_hero, stats_altered_by = command[0], command[1], int(command[2])

    if action == "CastSpell":
        spell_name = command[3]
        heroes_info = cast_spell(heroes_info, name_hero, stats_altered_by, spell_name)
    elif action == "TakeDamage":
        attacker = command[3]
        heroes_info = take_damage(heroes_info, name_hero, stats_altered_by, attacker)
    elif action == "Recharge":
        heroes_info = recharge(heroes_info, name_hero, stats_altered_by)
    elif action == "Heal":
        heroes_info = heal(heroes_info, name_hero, stats_altered_by)

    command = input()

for hero, hero_stat in heroes_info.items():
    print(f"{hero}\n  HP: {hero_stat['HP']}\n  MP: {hero_stat['MP']}")

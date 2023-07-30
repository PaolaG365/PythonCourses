def enroll(dictionary, name):
    if name not in dictionary:
        dictionary[name] = []
    else:
        print(f"{name} is already enrolled.")
    return dictionary


def learn(dictionary, name, spell):
    if name not in dictionary:
        print(f"{name} doesn't exist.")
    elif spell in dictionary[name]:
        print(f"{name} has already learned {spell}")
    else:
        dictionary[name].append(spell)
    return dictionary


def unlearn(dictionary, name, spell):
    if name not in dictionary:
        print(f"{name} doesn't exist.")
    elif spell not in dictionary[name]:
        print(f"{name} doesn't know {spell}")
    else:
        dictionary[name].remove(spell)
    return dictionary


heroes_spellbook = {}

command = input()

while command != "End":
    command = command.split()
    action, hero_name = command[0], command[1]

    if action == "Enroll":
        heroes_spellbook = enroll(heroes_spellbook, hero_name)
    elif action == "Learn":
        spell_name = command[2]
        heroes_spellbook = learn(heroes_spellbook, hero_name, spell_name)
    elif action == "Unlearn":
        spell_name = command[2]
        heroes_spellbook = unlearn(heroes_spellbook, hero_name, spell_name)

    command = input()

print("Heroes:")
for hero, hero_spells in heroes_spellbook.items():
    print(f"== {hero}: {', '.join(hero_spells)}")

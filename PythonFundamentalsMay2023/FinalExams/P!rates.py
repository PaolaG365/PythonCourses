def plunder(dictionary, target, people_killed, stolen_gold):
    dictionary[target]['population'] -= people_killed
    dictionary[target]['gold'] -= stolen_gold
    print(f"{target} plundered! {stolen_gold} gold stolen, {people_killed} citizens killed.")
    if dictionary[target]['population'] <= 0 or dictionary[target]['gold'] <= 0:
        print(f"{target} has been wiped off the map!")
        del dictionary[target]

    return dictionary


def prosper(dictionary, target, gold_increase):
    if gold_increase < 0:
        print("Gold added cannot be a negative number!")
    else:
        dictionary[target]['gold'] += gold_increase
        print(f"{gold_increase} gold added to the city treasury. {target} "
              f"now has {dictionary[target]['gold']} gold.")
    return dictionary


targeted_cities = {}
cities = input()

while cities != "Sail":
    cities = cities.split("||")
    city, population, gold = cities[0], int(cities[1]), int(cities[2])
    if city not in targeted_cities:
        targeted_cities[city] = {'population': population, 'gold': gold}
    else:
        targeted_cities[city]['population'] += population
        targeted_cities[city]['gold'] += gold

    cities = input()

command = input()

while command != "End":
    command = command.split("=>")
    action, town, amount_people_or_gold = command[0], command[1], int(command[2])

    if action == "Plunder":
        gold_stolen = int(command[3])
        targeted_cities = plunder(targeted_cities, town, amount_people_or_gold, gold_stolen)
    elif action == "Prosper":
        targeted_cities = prosper(targeted_cities, town, amount_people_or_gold)

    command = input()

if targeted_cities:
    print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")
    for town_name, town_info in targeted_cities.items():
        print(f"{town_name} -> Population: {town_info['population']} citizens, "
              f"Gold: {town_info['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

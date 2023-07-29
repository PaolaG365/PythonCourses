def is_valid_plant(dictionary, plant):
    if plant in dictionary:
        return True
    print("error")


def rate(dictionary, plant, new_rating):
    dictionary[plant]["rating"].append(new_rating)
    return dictionary


def update_dict(dictionary, plant, new_rarity):
    dictionary[plant]['rarity'] = new_rarity
    return dictionary


def reset(dictionary, plant):
    dictionary[plant]['rating'] = []
    return dictionary


lines = int(input())
plants_dict = {}

for _ in range(lines):
    initial_stats_plant = input().split("<->")
    plant_name, rarity = initial_stats_plant[0], int(initial_stats_plant[1])
    if plant_name not in plants_dict:
        plants_dict[plant_name] = {"rarity": 0}
    plants_dict[plant_name]["rarity"] = rarity
    plants_dict[plant_name]["rating"] = []

command = input()

while command != "Exhibition":
    action, target_action = command.split(": ")

    if action == "Rate":
        stats = target_action.split(" - ")
        name_plant, rating_stat = stats[0], int(stats[1])
        if is_valid_plant(plants_dict, name_plant):
            plants_dict = rate(plants_dict, name_plant, rating_stat)

    elif action == "Update":
        stats = target_action.split(" - ")
        name_plant, updated_rarity = stats[0], int(stats[1])
        if is_valid_plant(plants_dict, name_plant):
            plants_dict = update_dict(plants_dict, name_plant, updated_rarity)

    elif action == "Reset":
        name_plant = target_action
        if is_valid_plant(plants_dict, name_plant):
            plants_dict = reset(plants_dict, name_plant)

    command = input()

print(f"Plants for the exhibition:")
for plant_discovered, plant_stats in plants_dict.items():
    average_rating = 0
    if plant_stats['rating']:
        average_rating = sum(plant_stats['rating']) / len(plant_stats['rating'])
    print(f"- {plant_discovered}; Rarity: {plant_stats['rarity']}; Rating: {average_rating:.2f}")

def loot(chest, gained_loot):
    for item in gained_loot:
        if item not in chest:
            chest.insert(0, item)
    return chest


def drop(chest, target_index):
    if 0 <= target_index < len(chest):
        chest.append(chest.pop(target_index))
    return chest


def you_have_been_robbed(chest, stolen_items_num):
    if stolen_items_num >= len(chest):
        stolen_loot = chest.copy()
        chest.clear()
    else:
        stolen_loot = chest[-stolen_items_num:]
        chest = chest[:-stolen_items_num]
    print(", ".join(stolen_loot))
    return chest


treasure_chest = input().split("|")

command = input()

while command != "Yohoho!":
    command = command.split()
    action = command[0]

    if action == "Loot":
        loot_added = command[1:]
        treasure_chest = loot(treasure_chest, loot_added)
    elif action == "Drop":
        index = int(command[1])
        treasure_chest = drop(treasure_chest, index)
    elif action == "Steal":
        number_of_stolen_loot = int(command[1])
        treasure_chest = you_have_been_robbed(treasure_chest, number_of_stolen_loot)

    command = input()

if treasure_chest:
    total_gains = sum([len(x) for x in treasure_chest])
    average_gains = total_gains / len(treasure_chest)
    print(f"Average treasure gain: {average_gains:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

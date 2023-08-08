def is_valid_item(inventory, searched_item): return True if searched_item in inventory else False


def collect(inventory, searched_item):
    if not is_valid_item(inventory, searched_item):
        inventory.append(searched_item)
    return inventory


def drop(inventory, searched_item):
    if is_valid_item(inventory, searched_item):
        inventory.remove(searched_item)
    return inventory


def combine_items(inventory, first_item, second_item):
    if is_valid_item(inventory, first_item):
        inventory.insert(inventory.index(first_item) + 1, second_item)
    return inventory


def renew(inventory, searched_item):
    if is_valid_item(inventory, searched_item):
        inventory.remove(searched_item)
        inventory.append(searched_item)
    return inventory


loot_inventory = input().split(", ")

command = input()

while command != "Craft!":
    action, item = command.split(" - ")
    if action == "Collect":
        loot_inventory = collect(loot_inventory, item)
    elif action == "Drop":
        loot_inventory = drop(loot_inventory, item)
    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        loot_inventory = combine_items(loot_inventory, old_item, new_item)
    elif action == "Renew":
        loot_inventory = renew(loot_inventory, item)

    command = input()

print(", ".join(loot_inventory))

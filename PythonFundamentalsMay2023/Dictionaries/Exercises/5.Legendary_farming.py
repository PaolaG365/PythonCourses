inventory_items = {'shards': 0, 'fragments': 0, 'motes': 0}
legendary_obtained = False
type_legendary = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
legendary = ""

while not legendary_obtained:
    obtained_fragments = input().split()
    for index in range(0, len(obtained_fragments), 2):
        name = obtained_fragments[index + 1].lower()
        quantity_item = int(obtained_fragments[index])
        if name not in inventory_items:
            inventory_items[name] = 0
        inventory_items[name] += quantity_item
        if inventory_items[name] >= 250 and name in type_legendary:
            inventory_items[name] -= 250
            legendary_obtained = True
            legendary = type_legendary.get(name)
            break

print(f"{legendary} obtained!")
[print(f"{material}: {quantity}") for material, quantity in inventory_items.items()]

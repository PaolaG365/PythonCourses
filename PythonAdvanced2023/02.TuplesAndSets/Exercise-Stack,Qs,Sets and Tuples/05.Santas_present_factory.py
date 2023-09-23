from collections import deque

materials_values = deque(int(x) for x in input().split())
magic_values = deque(int(x) for x in input().split())
crafted_present = False

craft_recipe_cost = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

crafted_items = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0,
}

while magic_values and materials_values:
    material_value = materials_values.pop() if magic_values[0] or not materials_values[0] else 0
    magic_value = magic_values.popleft() if material_value or not magic_values[0] else 0

    if not magic_value:
        continue

    if material_value < 0 or magic_value < 0:
        materials_values.append(material_value + magic_value)
    elif material_value * magic_value not in craft_recipe_cost and material_value * magic_value > 0:
        materials_values.append(material_value + 15)
    else:
        crafted_items[craft_recipe_cost[material_value * magic_value]] += 1

    if crafted_items['Doll'] >= 1 and crafted_items["Wooden train"] >= 1:
        crafted_present = True
    elif crafted_items["Teddy bear"] >= 1 and crafted_items["Bicycle"] >= 1:
        crafted_present = True

print("The presents are crafted! Merry Christmas!") if crafted_present \
    else print("No presents this Christmas!")
if materials_values:
    print("Materials left: ", end="")
    print(*reversed(materials_values), sep=', ')
if magic_values:
    print("Magic left: ", end="")
    print(*magic_values, sep=", ")

for item, count in sorted(crafted_items.items()):
    if count > 0:
        print(f"{item}: {count}")


'''

from collections import deque

materials_values = deque(int(x) for x in input().split())
magic_values = deque(int(x) for x in input().split())
crafted_present = False

craft_recipe_cost = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

crafted_items = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0,
}

while magic_values and materials_values:
    material_value = materials_values.pop()
    magic_value = magic_values.popleft()

    if material_value < 0 or magic_value < 0:
        materials_values.append(material_value + magic_value)
    elif material_value * magic_value not in craft_recipe_cost and material_value * magic_value > 0:
        materials_values.append(material_value + 15)
    elif material_value == 0 or magic_value == 0:
        if magic_value == 0 and material_value == 0:
            continue
        elif material_value == 0:
            magic_values.appendleft(magic_value)
        elif magic_value == 0:
            materials_values.append(material_value)
        continue
    else:
        crafted_items[craft_recipe_cost[material_value * magic_value]] += 1

    if crafted_items['Doll'] >= 1 and crafted_items["Wooden train"] >= 1:
        crafted_present = True
    elif crafted_items["Teddy bear"] >= 1 and crafted_items["Bicycle"] >= 1:
        crafted_present = True

print("The presents are crafted! Merry Christmas!") if crafted_present \
    else print("No presents this Christmas!")
if materials_values:
    print("Materials left: ", end="")
    print(*reversed(materials_values), sep=', ')
if magic_values:
    print("Magic left: ", end="")
    print(*magic_values, sep=", ")

for item, count in sorted(crafted_items.items()):
    if count > 0:
        print(f"{item}: {count}")


'''
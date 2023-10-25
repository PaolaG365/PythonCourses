from collections import deque

items_info = {
    "Patch": {"needed resources": 30, "items_made": 0},
    "Bandage": {"needed resources": 40, "items_made": 0},
    "MedKit": {"needed resources": 100, "items_made": 0}
}

textiles = deque(int(x) for x in input().split())
medicaments = deque(int(x) for x in input().split())

while textiles and medicaments:
    fiber = textiles.popleft()
    med = medicaments.pop()
    result = fiber + med
    item_made = False

    for item in items_info:
        if result == items_info[item]["needed resources"]:
            items_info[item]["items_made"] += 1
            item_made = True
            break

    if result > items_info["MedKit"]["needed resources"]:
        item_made = True
        items_info["MedKit"]["items_made"] += 1
        remaining = result - items_info["MedKit"]["needed resources"]
        medicaments.append(remaining + medicaments.pop())

    if not item_made:
        medicaments.append(med + 10)


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for med_item, info in sorted(items_info.items(), key=lambda x: (-x[1]["items_made"], x[0])):
    if info["items_made"] > 0:
        print(f"{med_item} - {info['items_made']}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")

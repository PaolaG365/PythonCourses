def shop_from_grocery_list(budget: int, *groceries_info):
    grocery_list = groceries_info[0]
    purchased_list = []
    # why this work I have no idea, it shouldn't, but I guess...
    for item_info in range(1, len(groceries_info)):
        if groceries_info[item_info][0] in grocery_list and groceries_info[item_info][0] not in purchased_list:
            if budget >= groceries_info[item_info][1]:
                budget -= groceries_info[item_info][1]
                purchased_list.append(groceries_info[item_info][0])
                grocery_list.remove(groceries_info[item_info][0])
            else:
                break
    if grocery_list:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
    else:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

bakery_ingredients = input().split()
check_stock_for = input().split()
stock = {}

for item in range(0, len(bakery_ingredients), 2):
    name_ingredient = bakery_ingredients[item]
    in_stock = int(bakery_ingredients[item + 1])
    stock[name_ingredient] = in_stock

for searched_item in check_stock_for:
    if searched_item in stock:
        if stock[searched_item] > 0:  # value of the key - ingredient
            print(f"We have {stock[searched_item]} of {searched_item} left")
    else:
        print(f"Sorry, we don't have {searched_item}")

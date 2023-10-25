limits = {
    "Soup": 3,
    "Pizza": 4,
    "Dessert": 2,
}


def shopping_cart(*args):
    cart = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }
    result = []
    for info in args:
        if info == "Stop":
            break
        type_meal, meal = info
        if meal not in cart[type_meal] and len(cart[type_meal]) < limits[type_meal]:
            cart[type_meal].append(meal)

    if any(cart.values()):
        for meal_type, product in sorted(cart.items(), key=lambda x: (-len(x[1]), x[0], x[1].sort())):
            result.append(f"{meal_type}:")
            [result.append(f" - {food}") for food in product]
    else:
        result.append("No products in the cart!")

    return '\n'.join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print()
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print()
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

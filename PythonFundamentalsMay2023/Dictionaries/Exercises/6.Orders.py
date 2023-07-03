orders_dict = {}

command = input()

while command != "buy":
    command = command.split()
    product, price, quantity = command[0], float(command[1]), int(command[2])

    if product not in orders_dict:
        orders_dict[product] = {f'price {product}': 0.1, f'quantity {product}': 0}

    orders_dict[product][f'price {product}'] = price
    orders_dict[product][f'quantity {product}'] += quantity

    command = input()

# print(orders_dict)

for product_name, value in orders_dict.items():
    price_order = value[f'price {product_name}'] * value[f'quantity {product_name}']
    print(f"{product_name} -> {price_order:.2f}")

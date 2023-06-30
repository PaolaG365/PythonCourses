bakery_goods = input().split()
bakery = {}

for item in range(0, len(bakery_goods), 2):
    key_ingredient = bakery_goods[item]
    value_quantity = int(bakery_goods[item + 1])
    bakery[key_ingredient] = value_quantity

print(bakery)

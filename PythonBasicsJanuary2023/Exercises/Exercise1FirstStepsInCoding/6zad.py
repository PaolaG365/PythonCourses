nylon = int(input())
paint = int(input())
thinner = int(input())
hours_to_finish = int(input())

NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
THINNER_PRICE = 5.00
BAGS_PRICE = 0.40

nylon += 2
paint += paint * 0.10

materials_price = nylon * NYLON_PRICE + paint * PAINT_PRICE + thinner * THINNER_PRICE + BAGS_PRICE
workers_fee = (materials_price * 0.30) * hours_to_finish
total = materials_price + workers_fee

print(total)

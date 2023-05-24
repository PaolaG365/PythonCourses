veggies_kg_price, fruits_kg_price = float(input()), float(input())
kg_veggies, kg_fruits = int(input()), int(input())

EURO = 1.94

total = (kg_veggies * veggies_kg_price + kg_fruits * fruits_kg_price) / EURO

print(f'{total:.2f}')

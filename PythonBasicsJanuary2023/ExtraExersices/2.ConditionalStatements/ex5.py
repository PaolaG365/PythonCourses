import math

days_off, food_left = int(input()), int(input())
dog_food, cat_food = float(input()), float(input())
turtle_food = float(input()) / 1000

needed_total = days_off * dog_food + days_off * cat_food + days_off * turtle_food

if food_left >= needed_total:
    print(f'{math.floor(food_left - needed_total)} kilos of food left.')
else:
    print(f'{math.ceil(needed_total - food_left)} more kilos of food are needed.')

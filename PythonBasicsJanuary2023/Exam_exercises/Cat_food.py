number_cats = int(input())

small_cats, big_cats, huge_cats = 0, 0, 0
total_food_eaten = 0

for _ in range(number_cats):
    food_cat = float(input())
    total_food_eaten += food_cat

    if 100 <= food_cat < 200:
        small_cats += 1
    elif 200 <= food_cat < 300:
        big_cats += 1
    elif 300 <= food_cat < 400:
        huge_cats += 1

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {huge_cats} cats.")
print(f"Price for food per day: {(total_food_eaten / 1000) * 12.45:.2f} lv.")

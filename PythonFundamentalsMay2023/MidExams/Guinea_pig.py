food, hay, cover = float(input()), float(input()), float(input())
guinea_pig_weight = float(input())
total_food = food * 1000
total_hay = hay * 1000
total_cover = cover * 1000
needed_cover = (guinea_pig_weight * 1000) / 3
days = 0

while days < 30:
    days += 1
    total_food -= 300
    if days % 2 == 0:
        total_hay -= (total_food * 0.05)
    if days % 3 == 0:
        total_cover -= needed_cover

    if total_cover <= 0 or total_hay <= 0 or total_food <=0:
        print("Merry must go to the pet store!")
        break
else:
    print(f"Everything is fine! Puppy is happy!"
          f" Food: {total_food / 1000:.2f},"
          f" Hay: {total_hay / 1000:.2f},"
          f" Cover: {total_cover / 1000:.2f}.")

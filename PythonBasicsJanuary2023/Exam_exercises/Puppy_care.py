dog_food = int(input()) * 1000

eaten_food = 0

action = input()

while action != "Adopted":
    eaten_food += int(action)

    action = input()

if eaten_food <= dog_food:
    print(f"Food is enough! Leftovers: {dog_food - eaten_food} grams.")
else:
    print(f"Food is not enough. You need {eaten_food - dog_food} grams more.")

target_goal = int(input())

daily_total = 0
action = input()

while action != "closed":

    if action == "haircut":
        type_haircut = input()

        if type_haircut == "mens":
            daily_total += 15
        elif type_haircut == "ladies":
            daily_total += 20
        elif type_haircut == "kids":
            daily_total += 10

    elif action == "color":
        coloring = input()

        if coloring == "touch up":
            daily_total += 20
        elif coloring == "full color":
            daily_total += 30

    if daily_total >= target_goal:
        break

    action = input()

if daily_total >= target_goal:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {target_goal - daily_total}lv. more.")

print(f"Earned money: {daily_total}lv.")

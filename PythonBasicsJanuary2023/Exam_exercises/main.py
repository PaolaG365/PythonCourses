goal = int(input())
starting_height = goal - 30

fails, jumps = 0, 0
goal_reached = False

while fails < 3:
    jump_height = int(input())
    jumps += 1

    if jump_height > starting_height:
        if starting_height >= goal:
            goal_reached = True
            break
        starting_height += 5
        fails = 0

    else:
        fails += 1

if goal_reached:
    print(f"Tihomir succeeded, he jumped over {starting_height}cm after {jumps} jumps.")
else:
    print(f"Tihomir failed at {starting_height}cm after {jumps} jumps.")

STEPS_GOAL = 10000

total_steps = 0

while total_steps <= STEPS_GOAL:
    walked_steps = input()

    if walked_steps == "Going home":
        total_steps += int(input())

        if total_steps < STEPS_GOAL:
            print(f'{abs(total_steps - STEPS_GOAL)} more steps to reach goal.')
            break
    else:
        total_steps += int(walked_steps)

else:
    print(f'Goal reached! Good job!\n{total_steps - STEPS_GOAL} steps over the goal!')

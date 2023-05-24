actor_name = input()
academy_points = float(input())
jury_number = int(input())

POINTS_NEEDED = 1250.5

for _ in range(jury_number):
    name_jury = input()
    points_given = float(input())
    academy_points += len(name_jury) * points_given / 2

    if academy_points > POINTS_NEEDED:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break

else:
    print(f"Sorry, {actor_name} you need {POINTS_NEEDED - academy_points:.1f} more!")

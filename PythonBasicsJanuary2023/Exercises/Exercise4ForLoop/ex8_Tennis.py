import math
tournaments = int(input())
points = int(input())

won_points = 0
wins_count = 0

for _ in range(tournaments):
    stage_tournament = input()

    if stage_tournament == "W":
        wins_count += 1
        won_points += 2000
    elif stage_tournament == "F":
        won_points += 1200
    elif stage_tournament == "SF":
        won_points += 720

print(f'Final points: {points + won_points}\nAverage points: '
      f'{math.floor(won_points / tournaments)}\n{wins_count / tournaments * 100:.2f}%')

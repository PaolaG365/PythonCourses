number_tournaments = int(input())

total_raised = 0
wins, loses = 0, 0

for days in range(number_tournaments):
    daily_raised = 0
    daily_wins, daily_loses = 0, 0

    while True:
        action = input()

        if action == "Finish":
            break

        result_from_sport = input()

        if result_from_sport == "win":
            daily_raised += 20
            daily_wins += 1

        elif result_from_sport == "lose":
            daily_loses += 1

    if daily_wins > daily_loses:
        wins += 1
        daily_raised *= 1.10
    else:
        loses += 1

    total_raised += daily_raised

if wins > loses:
    total_raised *= 1.20
    print(f"You won the tournament! Total raised money: {total_raised:.2f}")

elif wins < loses:
    print(f"You lost the tournament! Total raised money: {total_raised:.2f}")

locations_number = int(input())

for _ in range(locations_number):
    average_gold_expected_daily = float(input())
    days_on_location = int(input())
    gold_dug = 0

    for _ in range(days_on_location):
        gold_dug += float(input())

    average_daily = gold_dug / days_on_location

    if average_daily >= average_gold_expected_daily:
        print(f"Good job! Average gold per day: {average_daily:.2f}.")
    else:
        print(f"You need {abs(average_daily - average_gold_expected_daily):.2f} gold.")

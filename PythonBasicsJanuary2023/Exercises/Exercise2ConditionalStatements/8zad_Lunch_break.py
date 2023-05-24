import math

series = input()
episode_length, lunch_break = int(input()), int(input())

eating_lunch = lunch_break * 1 / 8
rest = lunch_break * 1 / 4
time_left = lunch_break - (eating_lunch + rest)

if time_left >= episode_length:
    a = time_left - episode_length
    a = math.ceil(a)
    print(f"You have enough time to watch {series} and left with {a} minutes free time.")
else:
    a = episode_length - time_left
    a = math.ceil(a)
    print(f"You don't have enough time to watch {series}, you need {a} more minutes.")

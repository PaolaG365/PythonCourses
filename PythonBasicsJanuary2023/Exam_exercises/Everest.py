days = 1
starting_point = 5_364
everest_height = 8_848

while starting_point <= everest_height:
    sleep = input()

    if sleep == "END" or days >= 5:
        break

    meters_hiked = int(input())

    if sleep == "Yes":
        days += 1

    starting_point += meters_hiked

if starting_point >= everest_height:
    print(f"Goal reached for {days} days!")
else:
    print(f"Failed!\n{starting_point}")

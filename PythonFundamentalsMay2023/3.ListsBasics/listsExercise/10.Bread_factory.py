working_day_events = input(). split("|")

total_energy = 100
last_event_energy = 0
coins = 100

for events in range(len(working_day_events)):
    event = working_day_events[events].split("-")
    event_cost = int(event[-1])

    if "rest" in event:
        last_event_energy = total_energy
        total_energy += event_cost
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - last_event_energy
        print(f"You gained {gained_energy} energy.\nCurrent energy: {total_energy}.")

    elif "order" in event:
        if total_energy >= 30:
            total_energy -= 30
            coins += event_cost
            print(f"You earned {event_cost} coins.")
        else:
            total_energy += 50
            print("You had to rest!")

    else:
        if event_cost <= coins:
            coins -= event_cost
            print(f"You bought {event[0]}.")
        else:
            print(f"Closed! Cannot afford {event[0]}.")
            exit()

else:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {total_energy}")

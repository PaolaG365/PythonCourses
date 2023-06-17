people_waiting_in_q = int(input())
wagons = [int(x) for x in input().split()]
max_seats = 4

for wagon in range(len(wagons)):
    free_space = max_seats - wagons[wagon]

    if people_waiting_in_q >= free_space:
        wagons[wagon] += free_space

    else:
        wagons[wagon] += people_waiting_in_q

    people_waiting_in_q -= free_space

if any(seats for seats in wagons if seats < max_seats) and people_waiting_in_q <= 0:
    print("The lift has empty spots!")
elif all(seats for seats in wagons if seats == max_seats) and people_waiting_in_q > 0:
    print(f"There isn't enough space! {people_waiting_in_q} people in a queue!")

print(*wagons)

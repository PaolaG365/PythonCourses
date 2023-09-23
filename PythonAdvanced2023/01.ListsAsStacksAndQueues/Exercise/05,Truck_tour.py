from collections import deque

pumps_number = int(input())
pumps_q = deque([int(x) for x in input().split()] for _ in range(pumps_number))
pumps_q_copy = pumps_q.copy()
index, fuel = 0, 0

while pumps_q_copy:
    available_fuel, distance_to_next_pump = pumps_q_copy.popleft()
    if fuel + int(available_fuel) >= int(distance_to_next_pump):
        fuel += int(available_fuel)
        fuel -= int(distance_to_next_pump)
    else:
        fuel = 0
        index += 1
        pumps_q.rotate(-1)
        pumps_q_copy = pumps_q.copy()

print(index)

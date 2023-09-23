from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
water_bottles_litres = deque([int(x) for x in input().split()])
wasted_water = 0

while water_bottles_litres:
    if not cups_capacity:
        break
    cup_to_be_filled = cups_capacity.popleft()
    while cup_to_be_filled > 0:
        bottle_used = water_bottles_litres.pop()
        if bottle_used > cup_to_be_filled:
            wasted_water += abs(bottle_used - cup_to_be_filled)
            cup_to_be_filled -= bottle_used
        else:
            cup_to_be_filled -= bottle_used


if water_bottles_litres:
    print("Bottles: ", end="")
    print(*water_bottles_litres, sep=" ")
else:
    print("Cups: ", end="")
    print(*cups_capacity, sep=" ")

print(f"Wasted litters of water: {wasted_water}")

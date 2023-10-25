from collections import deque

initial_fuel = deque(int(x) for x in input().split())
additional_cons = deque(int(x) for x in input().split())
needed_fuel_to_checkpoint = deque(int(x) for x in input().split())
reached_altitudes = []

while initial_fuel and additional_cons:
    car_fuel = initial_fuel.pop()
    fuel_consumption = additional_cons.popleft()
    result = car_fuel - fuel_consumption

    if result < needed_fuel_to_checkpoint[0]:
        print(f"John did not reach: Altitude {5 - len(needed_fuel_to_checkpoint)}")
        break
    else:
        print(f"John has reached: Altitude {5 - len(needed_fuel_to_checkpoint)}")
        reached_altitudes.append(f"Altitude {5 - len(needed_fuel_to_checkpoint)}")
        to_checkpoint = needed_fuel_to_checkpoint.popleft()

if not needed_fuel_to_checkpoint:
    print("John has reached all the altitudes and managed to reach the top!")
elif needed_fuel_to_checkpoint and reached_altitudes:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached_altitudes)}")
elif not reached_altitudes:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

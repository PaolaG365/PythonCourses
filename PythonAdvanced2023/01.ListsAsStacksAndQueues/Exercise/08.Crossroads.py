from collections import deque

green_light, free_window = int(input()), int(input())
crossroad_queue = deque()
cars_passed = 0

command = input()
while command != "END":
    if command != "green":
        crossroad_queue.append(command)
    else:
        green_light_counter = green_light

        while green_light_counter > 0 and crossroad_queue:
            car = crossroad_queue.popleft()

            if len(car) > green_light_counter + free_window:
                print("A crash happened!")
                print(f"{car} was hit at {car[free_window + green_light_counter]}.")
                exit()

            green_light_counter -= len(car)
            cars_passed += 1

    command = input()

print(f"Everyone is safe.\n{cars_passed} total cars passed the crossroads.")

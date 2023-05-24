import math

width, length, height = float(input()), float(input()), float(input())
average_height = float(input())

ship_volume = width * length * height
room_volume = (average_height + 0.40) * 2 * 2
astronauts = math.floor(ship_volume / room_volume)

if astronauts < 3:
    print("The spacecraft is too small.")
elif astronauts > 10:
    print("The spacecraft is too big.")
else:
    print(f"The spacecraft holds {astronauts} astronauts.")

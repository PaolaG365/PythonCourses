lines = int(input())

cars_parked = set()

for _ in range(lines):
    action, car_number = input().split(", ")
    if action == "IN":
        cars_parked.add(car_number)
    elif action == "OUT":
        cars_parked.discard(car_number)

if cars_parked:
    print(*cars_parked, sep="\n")
else:
    print("Parking Lot is Empty")

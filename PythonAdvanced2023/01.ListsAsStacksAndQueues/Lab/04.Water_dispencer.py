from collections import deque
water_in_dispenser = int(input())
names_q = deque()

names = input()
while names != "Start":
    names_q.append(names)
    names = input()

command = input()
while command != "End":
    command = command.split()
    if len(command) == 1:
        if water_in_dispenser >= int(command[0]):
            print(f"{names_q.popleft()} got water")
            water_in_dispenser -= int(command[0])
        else:
            print(f"{names_q.popleft()} must wait")
    elif command[0] == "refill":
        water_in_dispenser += int(command[1])
    command = input()

print(f"{water_in_dispenser} liters left")

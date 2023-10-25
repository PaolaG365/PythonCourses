from collections import deque

seats = input().split(", ")
first_nums = deque(int(x) for x in input().split(", "))
second_nums = deque(int(x) for x in input().split(", "))
seat_matches = []
all_possible_seats_matched = False
rotations = 0

while rotations < 10:
    if len(seat_matches) == 3:
        all_possible_seats_matched = True
        break

    num1 = first_nums.popleft()
    num2 = second_nums.pop()
    letter = chr(num2 + num1)
    seat1 = str(num1) + letter
    seat2 = str(num2) + letter

    if seat2 in seat_matches or seat1 in seat_matches:
        rotations += 1
        continue
    elif seat1 in seats:
        seat_matches.append(seat1)
    elif seat2 in seats:
        seat_matches.append(seat2)
    else:
        first_nums.append(num1)
        second_nums.appendleft(num2)

    rotations += 1

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")

from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))
milkshakes_counter = 0

while milkshakes_counter < 5:
    if not chocolates or not cups_of_milk:
        break

    chocolate = chocolates[-1]
    cup_of_milk = cups_of_milk[0]

    if chocolate <= 0 or cup_of_milk <= 0:
        if cup_of_milk <= 0:
            cups_of_milk.popleft()
        if chocolate <= 0:
            chocolates.pop()
        continue

    if chocolate == cup_of_milk:
        milkshakes_counter += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.rotate(-1)
        chocolates[-1] -= 5

if milkshakes_counter >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print("Chocolate: ", end="")
print(*chocolates, sep=', ') if chocolates else print("empty")

print("Milk: ", end="")
print(*cups_of_milk, sep=', ') if cups_of_milk else print("empty")

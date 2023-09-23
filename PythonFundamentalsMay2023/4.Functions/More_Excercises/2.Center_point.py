import math


def closest_to_center(x11, y11, x22, y22):
    distance1 = abs(x11) + abs(y11)
    distance2 = abs(x22) + abs(y22)

    if distance1 <= distance2:
        print(f"({math.floor(x11)}, {math.floor(y11)})")
    else:
        print(f"({math.floor(x22)}, {math.floor(y22)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

closest_to_center(x1, y1, x2, y2)

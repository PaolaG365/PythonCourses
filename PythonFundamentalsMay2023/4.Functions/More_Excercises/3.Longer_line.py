import math


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    line1_point1 = abs(x1) + abs(y1)
    line1_point2 = abs(x2) + abs(y2)
    line2_point1 = abs(x3) + abs(y3)
    line2_point2 = abs(x4) + abs(y4)
    line1_sum = line1_point1 + line1_point2
    line2_sum = line2_point1 + line2_point2
    if line1_sum >= line2_sum:
        if line1_point1 <= line1_point2:
            print(f"({math.floor(x1)}, {math.floor(y1)})", end="")
            print(f"({math.floor(x2)}, {math.floor(y2)})")
        else:
            print(f"({math.floor(x2)}, {math.floor(y2)})", end="")
            print(f"({math.floor(x1)}, {math.floor(y1)})")
    else:
        if line2_point1 <= line2_point2:
            print(f"({math.floor(x3)}, {math.floor(y3)})", end="")
            print(f"({math.floor(x4)}, {math.floor(y4)})")
        else:
            print(f"({math.floor(x4)}, {math.floor(y4)})", end="")
            print(f"({math.floor(x3)}, {math.floor(y3)})")


x1_1, y1_1 = float(input()), float(input())
x1_2, y1_2 = float(input()), float(input())
x2_1, y2_1 = float(input()), float(input())
x2_2, y2_2 = float(input()), float(input())

longer_line(x1_1, y1_1, x1_2, y1_2, x2_1, y2_1, x2_2, y2_2)

x1, y1, x2, y2, x, y = float(input()), float(input()), float(input()), float(input()),\
    float(input()), float(input())

if ((x == x1 or x == x2) and y1 <= y <= y2) or \
      ((y == y1 or y == y2) and x1 <= x <= x2):
    print("Border")
else:
    print('Inside / Outside')
    
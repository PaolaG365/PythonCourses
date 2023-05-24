x, y, h = float(input()), float(input()), float(input())

ONE_LITER_GREEN = 3.4
ONE_LITER_RED = 4.3

door = 1.2 * 2
windows = 2 * (1.5 * 1.5)

square_walls = 2 * (x * x) - door
side_walls = 2 * (x * y) - windows
green_paint_used = (square_walls + side_walls) / ONE_LITER_GREEN

roof_rectangles = 2 * (x * y)
roof_triangle = 2 * (x * h/2)
red_paint_used = (roof_triangle + roof_rectangles) / ONE_LITER_RED

print(f"{green_paint_used:.2f}\n{red_paint_used:.2f}")

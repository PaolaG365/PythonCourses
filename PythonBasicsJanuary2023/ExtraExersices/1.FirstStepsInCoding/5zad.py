w, h = float(input()), float(input())

ONE_WORK_SPACE_H = 70
ONE_WORK_SPACE_W = 120

desks_on_row = ((h * 100) - 100) // ONE_WORK_SPACE_H
rows = (w * 100) // ONE_WORK_SPACE_W

total_space = (desks_on_row * rows) - 3

print(f"{total_space:.0f}")

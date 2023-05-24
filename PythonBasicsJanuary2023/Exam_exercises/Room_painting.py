import math

paint, tapestries = int(input()), int(input())
gloves_cost, brush_cost = float(input()), float(input())

total_paint = paint * 21.50
tapestries_total = tapestries * 5.20
gloves_total = math.ceil(tapestries * 0.35) * gloves_cost
brush_total = math.floor(paint * 0.48) * brush_cost
total = total_paint + tapestries_total + gloves_total + brush_total

print(f"This delivery will cost {total / 15:.2f} lv.")

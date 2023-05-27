fires = input().split("#")
water = int(input())
effort, total_fires = 0, 0
cells = []

for fire in range(len(fires)):
    list_fire = fires[fire].split(" = ")
    range_fire = int(list_fire[-1])

    if "High" in list_fire and 81 <= range_fire <= 125:
        cells.append(range_fire)
        effort += range_fire * 0.25
        total_fires += range_fire
        water -= range_fire
    if "Medium" in list_fire and 51 <= range_fire <= 80:
        cells.append(range_fire)
        effort += range_fire * 0.25
        total_fires += range_fire
        water -= range_fire
    if "Low" in list_fire and 1 <= range_fire <= 50:
        cells.append(range_fire)
        effort += range_fire * 0.25
        total_fires += range_fire
        water -= range_fire
    if water < 0:
        cells.pop(-1)
        effort -= range_fire * 0.25
        total_fires -= range_fire
        water += range_fire
        continue
    elif water == 0:
        break


print(f"Cells:")
for cell in cells:
    print(f"- {cell}")

print(f"Effort: {effort:.2f}\nTotal Fire: {total_fires}")

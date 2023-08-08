pirating_days = int(input())
plunder_daily = int(input())
expected_plunder = float(input())
total_plunder_gained = 0

for day in range(1, pirating_days + 1):
    total_plunder_gained += plunder_daily
    if day % 3 == 0:
        total_plunder_gained += (plunder_daily * 0.5)
    if day % 5 == 0:
        total_plunder_gained -= (total_plunder_gained * 0.3)

if total_plunder_gained >= expected_plunder:
    print(f"Ahoy! {total_plunder_gained:.2f} plunder gained.")
else:
    percentage_left = (total_plunder_gained / expected_plunder) * 100
    print(f"Collected only {percentage_left:.2f}% of the plunder.")

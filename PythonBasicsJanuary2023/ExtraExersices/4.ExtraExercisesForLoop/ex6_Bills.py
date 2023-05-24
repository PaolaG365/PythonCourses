months = int(input())

electricity, water, internet, other = 0, 0, 0, 0
total = 0

for _ in range(months):
    electricity_bill = float(input())
    electricity += electricity_bill
    water += 20
    internet += 15
    other_bill = (electricity_bill + 20 + 15) * 1.2
    other += other_bill
    total += electricity_bill + 20 + 15 + other_bill

print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f"Average: {total / months:.2f} lv")

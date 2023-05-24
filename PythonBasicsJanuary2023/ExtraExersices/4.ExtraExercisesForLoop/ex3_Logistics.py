number_deliveries = int(input())

delivered_tons = 0
van = 0
truck = 0
train = 0
total_price = 0

for _ in range(number_deliveries):
    tons_daily = int(input())
    delivered_tons += tons_daily
    if tons_daily < 4:
        van += tons_daily
        total_price += tons_daily * 200
    elif tons_daily < 12:
        truck += tons_daily
        total_price += tons_daily * 175
    else:
        train += tons_daily
        total_price += tons_daily * 120

print(f"{total_price / delivered_tons:.2f}")
print(f"{van / delivered_tons * 100:.2f}%")
print(f"{truck / delivered_tons * 100:.2f}%")
print(f"{train / delivered_tons * 100:.2f}%")

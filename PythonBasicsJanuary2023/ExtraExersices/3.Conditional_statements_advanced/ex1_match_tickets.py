budget = float(input())
category = input()
group_members = int(input())

transport_price = 0
tickets_price = 0

if 1 <= group_members <= 4:
    transport_price = budget * 0.75
elif 5 <= group_members <= 9:
    transport_price = budget * 0.6
elif 10 <= group_members <= 24:
    transport_price = budget * 0.5
elif 25 <= group_members <= 49:
    transport_price = budget * 0.4
else:
    transport_price = budget * 0.25

if category == "VIP":
    tickets_price = group_members * 499.99
elif category == "Normal":
    tickets_price = group_members * 249.99

total = transport_price + tickets_price

if total < budget:
    print(f"Yes! You have {budget - total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva.")

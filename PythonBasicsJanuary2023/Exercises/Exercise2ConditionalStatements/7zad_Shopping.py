budget = float(input())
graphic_cards, processors, ram = int(input()), int(input()), int(input())

gpu_price = graphic_cards * 250
processor_price = gpu_price * 0.35
ram_price = gpu_price * 0.1
total = gpu_price + processors * processor_price + ram * ram_price

if graphic_cards > processors:
    total = total - total * 0.15

if total <= budget:
    a = budget - total
    print(f'You have {a:.2f} leva left!')
else:
    a = total - budget
    print(f'Not enough money! You need {a:.2f} leva more!')

age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_savings = 0
money_given = 10

for i in range(1, age + 1):
    if i % 2 == 0:
        total_savings += money_given - 1
        money_given += 10
    else:
        total_savings += toy_price

if total_savings >= washing_machine_price:
    print(f'Yes! {total_savings - washing_machine_price:.2f}')
else:
    print(f'No! {washing_machine_price - total_savings:.2f}')

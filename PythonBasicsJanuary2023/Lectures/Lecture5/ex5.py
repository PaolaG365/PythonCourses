bill = input()

total = 0.0

while bill != "NoMoreMoney":

    bills = float(bill)

    if bills < 0:
        print("Invalid operation!")
        break
    total += bills
    print(f'Increase: {bills:.2f}')
    bill = input()

print(f'Total: {total:.2f}')

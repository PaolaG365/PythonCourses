screening_type = input()
rows, columns = int(input()), int(input())

price = 0

if screening_type == "Premiere":
    price = 12.00
elif screening_type == "Normal":
    price = 7.50
elif screening_type == "Discount":
    price = 5.00

income = (rows * columns) * price

print(f"{income:.2f} leva")

import math

magnolias, hyacinths, roses, cacti = int(input()), int(input()), int(input()), int(input())
gift_price = float(input())

total_without_tax = magnolias * 3.25 + hyacinths * 4 + roses * 3.50 + cacti * 8
tax = total_without_tax * 0.05
income = total_without_tax - tax

if income >= gift_price:
    print(f'She is left with {math.floor(income - gift_price)} leva.')
else:
    print(f'She will have to borrow {math.ceil(gift_price - income)} leva.')

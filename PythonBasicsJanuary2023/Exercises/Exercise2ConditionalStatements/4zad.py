trip_price = float(input())
puzzles, talking_dolls, plush_bears, minions, trucks = int(input()), \
            int(input()), int(input()), int(input()), int(input())

PUZZLE_PRICE = 2.60
TD_PRICE = 3
PB_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

toys_price = puzzles * PUZZLE_PRICE + talking_dolls * TD_PRICE \
    + plush_bears * PB_PRICE + minions * MINION_PRICE + trucks * TRUCK_PRICE
number_of_toys = puzzles + talking_dolls + plush_bears + minions + trucks

if number_of_toys >= 50:
    toys_price -= toys_price * 0.25

shop_rent = toys_price * 0.1
money_won = toys_price - shop_rent

if money_won >= trip_price:
    a = money_won - trip_price
    print(f"Yes! {a:.2f} lv left.")
else:
    a = trip_price - money_won
    print(f"Not enough money! {a:.2f} lv needed.")

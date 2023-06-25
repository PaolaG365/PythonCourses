city_count = int(input())
total_profit = 0

for city in range(1, city_count + 1):
    name_city = input()
    income = float(input())
    expenses = float(input())
    profit = 0

    if city % 5 == 0:
        income -= income * 0.1

    elif city % 3 == 0:
        expenses += expenses * 0.5

    profit = income - expenses

    total_profit += profit

    print(f"In {name_city} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")

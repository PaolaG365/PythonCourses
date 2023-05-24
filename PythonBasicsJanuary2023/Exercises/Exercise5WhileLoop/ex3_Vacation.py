vacation_money, total_money = float(input()), float(input())

days_counter = 0
spend_counter = 0

while True:
    spend_or_save = input()
    money = float(input())
    days_counter += 1

    if spend_or_save == "spend":
        total_money -= money if total_money > money else 0
        spend_counter += 1

    else:
        total_money += money
        spend_counter = 0

    if spend_counter == 5:
        print(f"You can't save the money.\n{days_counter}")
        break

    if total_money >= vacation_money:
        print(f'You saved the money for {days_counter} days.')
        break

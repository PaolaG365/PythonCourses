fruit, day = input(), input()
quantity = float(input())

price = 0
total_price = 0

if (day != 'Monday' and day != "Tuesday" and day != 'Wednesday' and day != 'Thursday' and day != "Friday" and
    day != "Saturday" and day != "Sunday") or \
        (fruit != "banana" and fruit != 'apple' and
         fruit != 'orange' and fruit != 'grapefruit' and fruit != 'kiwi'
         and fruit != 'pineapple' and fruit != 'grapes'):
    print('error')

if day == 'Monday' or day == "Tuesday" or day == 'Wednesday' or day == 'Thursday' or day == "Friday":

    if fruit == "banana":
        price = 2.50
    elif fruit == 'apple':
        price = 1.20
    elif fruit == 'orange':
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.50
    elif fruit == 'grapes':
        price = 3.85
    total_price = price * quantity

if day == "Saturday" or day == "Sunday":

    if fruit == "banana":
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == 'kiwi':
        price = 3.00
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20
    total_price = price * quantity

if total_price != 0:
    print(f'{total_price:.2f}')

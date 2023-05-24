time = int(input())
day = input()

work_days = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday"

if day in work_days:
    if 10 <= time <= 18:
        print('open')
    else:
        print('closed')

if day == "Sunday":
    print('closed')

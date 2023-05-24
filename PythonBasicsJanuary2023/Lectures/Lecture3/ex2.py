day = input()

work_days = "Monday, Tuesday, Wednesday, Thursday, Friday"
weekend = "Saturday, Sunday"

if day in work_days:
    print('Working day')
elif day in weekend:
    print("Weekend")
else:
    print("Error")

month = input()
hours_gaming, people_in_group = int(input()), int(input())
time_of_the_day = input()

tax_one_person = 0

sping = ["march", "april", "may"]
summer = ["june", "july", "august"]

if time_of_the_day == "day":
    if month in sping:
        tax_one_person = 10.50
    elif month in summer:
        tax_one_person = 12.60

elif time_of_the_day == "night":
    if month in sping:
        tax_one_person = 8.40
    elif month in summer:
        tax_one_person = 10.20

if people_in_group >= 4:
    tax_one_person *= 0.9

if hours_gaming >= 5:
    tax_one_person *= 0.5

print(f"Price per person for one hour: {tax_one_person:.2f}")
print(f"Total cost of the visit: {tax_one_person * people_in_group * hours_gaming:.2f}")

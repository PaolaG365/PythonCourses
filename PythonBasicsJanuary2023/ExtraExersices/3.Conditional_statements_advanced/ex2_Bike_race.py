juniors_racers, senior_racers = int(input()), int(input())
race_type = input()

tax_junior = 0
tax_senior = 0

if race_type == "trail":
    tax_junior = 5.50
    tax_senior = 7
elif race_type == "cross-country":
    tax_junior = 8
    tax_senior = 9.50
elif race_type == "downhill":
    tax_junior = 12.25
    tax_senior = 13.75
elif race_type == "road":
    tax_junior = 20
    tax_senior = 21.50

total = juniors_racers * tax_junior + senior_racers * tax_senior

if race_type == "cross-country" and (juniors_racers + senior_racers) >= 50:
    total -= total * 0.25

print(f"{total - total * 0.05:.2f}")

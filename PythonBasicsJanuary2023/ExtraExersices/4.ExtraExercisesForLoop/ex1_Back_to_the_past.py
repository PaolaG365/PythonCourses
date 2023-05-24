rich_kid_money = float(input())
year_he_dies = int(input())

KID_AGE = 18

for age in range(1800, year_he_dies + 1):

    if age % 2 == 0:
        rich_kid_money -= 12000
        KID_AGE += 1
    else:
        rich_kid_money -= 12000 + 50 * KID_AGE
        KID_AGE += 1

if 0 <= rich_kid_money:
    print(f"Yes! He will live a carefree life and will have {abs(rich_kid_money):.2f}"
          f" dollars left.")
else:
    print(f"He will need {abs(rich_kid_money):.2f} dollars to survive.")

wealth_people = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())

for money_per_person in range(len(wealth_people)):  # takes from the rich and gives to the poor...
    if wealth_people[money_per_person] < minimum_wealth:
        needed_money = minimum_wealth - wealth_people[money_per_person]
        wealth_people[wealth_people.index(max(wealth_people))] -= needed_money
        wealth_people[money_per_person] += needed_money

if any([x for x in wealth_people if x < minimum_wealth]):
    print("No equal distribution possible")
else:
    print(wealth_people)

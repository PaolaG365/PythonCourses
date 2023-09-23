lines = int(input())
odds = set()
evens = set()

for line in range(1, lines + 1):
    name_value = sum([ord(ch) for ch in input()]) // line
    evens.add(name_value) if name_value % 2 == 0 else odds.add(name_value)

sum_odds = sum(odds)
sum_evens = sum(evens)

if sum_evens == sum_odds:
    print(*odds.union(evens), sep=', ')
elif sum_odds > sum_evens:
    print(*odds.difference(evens), sep=', ')
else:
    print(*evens.symmetric_difference(odds), sep=', ')

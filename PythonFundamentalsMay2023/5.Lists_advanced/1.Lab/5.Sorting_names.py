names = input().split(", ")
# python magic, sorts by length of word and x sorts alphabetically if same length
print(sorted(names, key=lambda x: (-len(x), x)))

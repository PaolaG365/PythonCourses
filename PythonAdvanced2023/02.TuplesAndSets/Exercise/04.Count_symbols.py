symbols = [el for el in input()]
unique_symbols = set(symbols)
counts = {}

for el in unique_symbols:
    counts.update({el: symbols.count(el)})

for el1 in sorted(counts):
    print(f"{el1}: {counts[el1]} time/s")

from collections import deque

bees_values = deque(int(x) for x in input().split())
nectar_values = deque(int(x) for x in input().split())
arithmetics_symbols = deque(el for el in input().split())
total_honey_made = 0

# we can collect half a nectar... doesn't say if its in grams or anything.....
map_arithmetics = {
    "+": lambda x: x[0] + x[1],
    "-": lambda x: x[0] - x[1],
    "*": lambda x: x[0] * x[1],
    "/": lambda x: x[0] / x[1],
}

while bees_values and nectar_values:
    bee = bees_values[0]
    nectar = nectar_values[-1]

    if nectar < bee:
        nectar_values.pop()
        continue
    else:
        arithmetics = arithmetics_symbols.popleft()
        if arithmetics == "/" and nectar == 0:
            bees_values.popleft()
            nectar_values.pop()
            continue
        total_honey_made += abs(map_arithmetics[arithmetics]([bee, nectar]))
        bees_values.popleft()
        nectar_values.pop()

print(f"Total honey made: {total_honey_made}")
if bees_values:
    print("Bees left: ", end='')
    print(*bees_values, sep=', ')
if nectar_values:
    print("Nectar left: ", end='')
    print(*nectar_values, sep=', ')

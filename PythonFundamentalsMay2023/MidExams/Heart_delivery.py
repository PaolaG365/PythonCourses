neighborhood = [int(x) for x in input().split("@")]
last_index = 0
command = input()

while command != "Love!":
    index = int(command.split()[-1]) + last_index
    if not 0 <= index < len(neighborhood):
        index = 0
    last_index = index
    if neighborhood[index] <= 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        neighborhood[index] -= 2
        if neighborhood[index] <= 0:
            print(f"Place {index} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {last_index}.")

non_celebrating_houses = list(filter(lambda x: x > 0, neighborhood))

if not non_celebrating_houses:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(non_celebrating_houses)} places.")

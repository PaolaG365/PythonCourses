rows_of_field = int(input())
# appends a list of input in n range to a list
ships_health = [[int(x) for x in input().split()] for _ in range(rows_of_field)]
attacks_index = input().split()
destroyed_ships = 0

for attack in range(len(attacks_index)):

    index_attack = attacks_index[attack].split("-")
    first_coordinate = int(index_attack[0])
    second_coordinate = int(index_attack[1])

    if ships_health[first_coordinate][second_coordinate] > 0:
        ships_health[first_coordinate][second_coordinate] -= 1
        if ships_health[first_coordinate][second_coordinate] == 0:
            destroyed_ships += 1

print(destroyed_ships)

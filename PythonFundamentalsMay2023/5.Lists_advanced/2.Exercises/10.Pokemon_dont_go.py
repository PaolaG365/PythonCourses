def sum_of_pokemons(pokemons, index_pokemon):

    if index_pokemon < 0:
        current_pokemon = pokemons.pop(0)
        pokemons.insert(0, pokemons[-1])
    elif index_pokemon > len(pokemons) - 1:
        current_pokemon = pokemons.pop(-1)
        pokemons.append(pokemons[0])
    else:
        current_pokemon = pokemons.pop(index_pokemon)

    for pokemon in range(len(pokemons)):
        if pokemons[pokemon] <= current_pokemon:
            pokemons[pokemon] += current_pokemon
        else:
            pokemons[pokemon] -= current_pokemon

    return current_pokemon


pokemons_to_catch = [int(x) for x in input().split()]
pokemons_sum = 0

while pokemons_to_catch:
    index = int(input())
    pokemons_sum += sum_of_pokemons(pokemons_to_catch, index)

print(pokemons_sum)

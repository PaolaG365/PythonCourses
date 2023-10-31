from typing import List
from pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, caught_pokemon: Pokemon):
        if caught_pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(caught_pokemon)
        return f"Caught {caught_pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for pokemon_instance in self.pokemons:
            if pokemon_name == pokemon_instance.name:
                self.pokemons.remove(pokemon_instance)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        data = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        [data.append(f"- {pokemon.pokemon_details()}") for pokemon in self.pokemons]
        return "\n".join(data)

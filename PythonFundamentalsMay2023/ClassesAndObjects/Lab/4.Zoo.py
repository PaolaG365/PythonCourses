class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            print(f"Mammals in {self.name}: {', '.join(self.mammals)}")
        elif species == "fish":
            print(f"Fishes in {self.name}: {', '.join(self.fishes)}")
        elif species == "bird":
            print(f"Birds in {self.name}: {', '.join(self.birds)}")
        return f"Total animals: {Zoo.__animals}"


zoo_instance = Zoo(input())
animals_number = int(input())

for animal_num in range(animals_number):
    animal = input().split()
    animal_species = animal[0]
    animal_name = animal[1]
    zoo_instance.add_animal(animal_species, animal_name)

species_info_needed = input()

print(zoo_instance.get_info(species_info_needed))

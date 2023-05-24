length, width, height = int(input()), int(input()), int(input())
percent_occupied = float(input())

volume = length * width * height
tank_volume = volume / 1000
space_occupied = percent_occupied / 100
total_litre = tank_volume * (1 - space_occupied)

print(total_litre)

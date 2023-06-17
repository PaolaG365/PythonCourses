initial_energy = int(input())
distance_target_energy_cost = input()
battles_won = 0

while distance_target_energy_cost != "End of battle":
    distance_target_energy_cost = int(distance_target_energy_cost)
    battles_won += 1

    if distance_target_energy_cost <= initial_energy:
        initial_energy -= distance_target_energy_cost
    else:
        print(f"Not enough energy! Game ends with {battles_won - 1} won battles and {initial_energy} energy")
        exit()
        
    if battles_won % 3 == 0:
        initial_energy += battles_won

    distance_target_energy_cost = input()

print(f"Won battles: {battles_won}. Energy left: {initial_energy}")

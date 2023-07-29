def drive(dictionary, car_model, driving_distance, fuel_needed):
    if fuel_needed > dictionary[car_model]['fuel']:
        print("Not enough fuel to make that ride")
    else:
        dictionary[car_model]['mileage'] += driving_distance
        dictionary[car_model]['fuel'] -= fuel_needed
        print(f"{car_model} driven for {driving_distance} kilometers. "
              f"{fuel_needed} liters of fuel consumed.")
        if dictionary[car_model]['mileage'] >= 100_000:
            print(f"Time to sell the {car_model}!")
            del dictionary[car_model]
    return dictionary


def refuel(dictionary, car_model, fuel_added):

    if dictionary[car_model]['fuel'] + fuel_added >= 75:
        fuel_in = 75 - dictionary[car_model]['fuel']
        dictionary[car_model]['fuel'] += fuel_in
    else:
        fuel_in = fuel_added
        dictionary[car_model]['fuel'] += fuel_in
    print(f"{car_model} refueled with {fuel_in} liters")
    return dictionary


def revert(dictionary, car_model, reverted_km):
    if dictionary[car_model]['mileage'] - reverted_km < 10_000:
        dictionary[car_model]['mileage'] = 10_000
    else:
        dictionary[car_model]['mileage'] -= reverted_km
        print(f"{car_model} mileage decreased by {reverted_km} kilometers")
    return dictionary


number_of_cars = int(input())
cars_info = {}

for _ in range(number_of_cars):
    car = input().split("|")
    name, mileage, fuel = car[0], int(car[1]), int(car[2])
    if name not in cars_info:
        cars_info[name] = {}
    cars_info[name] = {"mileage": mileage, "fuel": fuel}

command = input()

while command != "Stop":
    command = command.split(" : ")
    action, car_name = command[0], command[1]

    if action == "Drive":
        distance, needed_fuel = int(command[2]), int(command[3])
        cars_info = drive(cars_info, car_name, distance, needed_fuel)
    elif action == "Refuel":
        added_fuel = int(command[2])
        cars_info = refuel(cars_info, car_name, added_fuel)
    elif action == "Revert":
        kilometers = int(command[2])
        cars_info = revert(cars_info, car_name, kilometers)
    command = input()

for model_car, info in cars_info.items():
    print(f"{model_car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel']} lt.")

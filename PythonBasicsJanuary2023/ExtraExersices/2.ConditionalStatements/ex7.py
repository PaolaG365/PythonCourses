fuel_type = input()
liters_fuel = float(input())

type_fuel = "Diesel, Gas, Gasoline"

if fuel_type not in type_fuel:
    print("Invalid fuel!")
else:
    if liters_fuel >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")

# if fuel_type == "Diesel" or fuel_type == "Gas" or fuel_type == "Gasoline":
#     if liters_fuel >= 25:
#         print(f"You have enough {fuel_type.lower()}.")
#     else:
#         print(f"Fill your tank with {fuel_type.lower()}!")
#
# else:
#     print('Invalid fuel!')

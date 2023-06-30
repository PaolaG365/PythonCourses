resources = {}

while True:
    command = input()

    if command == "stop":
        break

    quantity = int(input())

    if command not in resources:
        resources[command] = 0

    resources[command] += quantity

[print(f"{resource_name} -> {resource_quantity}") for resource_name, resource_quantity in resources.items()]

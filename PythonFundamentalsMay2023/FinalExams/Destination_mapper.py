import re

destinations = input()
destination_pattern = re.compile(r"(?P<sep>[=/])(?P<destination>[A-Z][A-Za-z]{2,})(?P=sep)")
valid_destinations = re.finditer(destination_pattern, destinations)
travel_points = 0
real_destinations = []

for destination in valid_destinations:
    real_destinations.append(destination.group('destination'))
    travel_points += len(destination.group('destination'))

print(f"Destinations: {', '.join(real_destinations)}")
print(f"Travel Points: {travel_points}")

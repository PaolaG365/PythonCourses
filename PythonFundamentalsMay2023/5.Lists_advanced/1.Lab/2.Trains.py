def add_people(vehicle, people):
    vehicle[-1] += people
    return vehicle


def insert_people(vehicle, index, people):
    vehicle[index] += people
    return vehicle


def leaving_people(vehicle, index, people):
    vehicle[index] -= people
    return vehicle


number_of_wagons = int(input())
train = [0] * number_of_wagons

command = input()

while command != "End":
    event = command.split()
    number_people = int(event[-1])

    if "add" in event:
        add_people(train, number_people)
    elif "insert" in event:
        wagon = int(event[1])
        insert_people(train, wagon, number_people)
    elif "leave" in event:
        wagon = int(event[1])
        leaving_people(train, wagon, number_people)

    command = input()

print(train)

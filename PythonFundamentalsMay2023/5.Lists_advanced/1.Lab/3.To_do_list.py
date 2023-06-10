to_do_list = [0] * 10
command = input()

while command != "End":
    event = command.split("-")
    to_do_list.pop(int(event[0])-1)
    to_do_list.insert(int(event[0]) - 1, event[1])

    command = input()

print([el for el in to_do_list if el != 0])

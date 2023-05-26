gifts_received = input().split(" ")
command = input()

while command != "No Money":
    list_command = command.split(" ")

    if "OutOfStock" in list_command:
        for gift in gifts_received:
            if list_command[1] in gifts_received:
                out_of_stock_gift = gifts_received.index(list_command[1])
                gifts_received[out_of_stock_gift] = "None"

    if "Required" in list_command:
        if 0 < int(list_command[-1]) <= len(gifts_received) - 1:
            gifts_received[int(list_command[-1])] = list_command[1]

    if "JustInCase" in list_command:
        gifts_received[-1] = list_command[-1]

    command = input()

for gifts in gifts_received:
    if gifts != "None":
        print(gifts, end=" ")

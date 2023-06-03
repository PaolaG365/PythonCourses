sequence_of_numbers = input().split()
received_message = input()
message = ''
list_of_received_message = []

for char in received_message:
    list_of_received_message.append(char)

for number in range(len(sequence_of_numbers)):
    index_letter = 0
    for num in sequence_of_numbers[number]:
        index_letter += int(num)

    if index_letter >= len(received_message):
        index_letter -= len(received_message)

    message += list_of_received_message[index_letter]
    list_of_received_message.remove(list_of_received_message[index_letter])

print(message)

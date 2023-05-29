sequence_of_numbers = input().split()
received_message = input()
message = ''

for number in range(len(sequence_of_numbers)):
    index_letter = 0
    for num in sequence_of_numbers[number]:
        index_letter += int(num)

    while index_letter >= 0:
        for el in received_message:
            index_letter -= 1
            if index_letter == 0:
                message += el
                received_message -= el
                break

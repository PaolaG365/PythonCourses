def merge(words, index1, index2):  # merge strings from list by index
    new_string = ''

    for index in range(index1, index2 + 1):
        new_string += words[index]

    # for word1 in words[index1 + 1: index2 + 1]:
    #     words.remove(word1)

    words[index1] = new_string

    return words


def divide(words, index, parts):
    pass


user_string = input().split()

command = input()

while command != "3:1":
    list_command = command.split()
    event = list_command[0]
    start_index = int(list_command[1])
    end_index_or_parts = int(list_command[2])

    if event == "merge":
        if end_index_or_parts >= len(user_string):
            end_index_or_parts = - 1

        if start_index >= len(user_string):
            start_index = 0
        merge(user_string, start_index, end_index_or_parts)

    elif event == "divide":
        pass

    command = input()


print(" ".join(user_string))

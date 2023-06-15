def merge(words, index1, index2):
    if index2 >= len(words):
        index2 = len(words) - 1
    if index1 < 0:
        index1 = 0
    new_word = "".join(words[index1:index2 + 1])
    words = words[:index1] + words[index2 + 1:]
    if new_word != "":
        words.insert(index1, new_word)
    return words


def divide(words, index, parts):  # divide string at n index into n parts
    word = [symbol for symbol in words.pop(index)]
    word_list = []

    if parts > len(word):
        length_part = 1
    else:
        length_part = int(len(word) / parts)
    starting_index = 0

    for symbol in range(parts):
        if symbol == parts - 1:
            word_list.append("".join(word[starting_index:]))
            break
        else:
            word_list.append("".join(word[starting_index:starting_index + length_part]))
        starting_index += length_part

    for el in word_list:
        words.insert(index, el)
        index += 1

    return words


threat_string = input().split()
command = input()

while command != "3:1":
    command = command.split()
    action = command[0]
    first_index = int(command[1])
    index_or_parts = int(command[2])

    if action == "merge":
        threat_string = merge(threat_string, first_index, index_or_parts)

    elif action == "divide":
        threat_string = divide(threat_string, first_index, index_or_parts)

    command = input()

print(" ".join(threat_string))

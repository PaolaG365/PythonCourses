def illusion(text, target_index, new_letter):
    text = text[:target_index] + new_letter + text[target_index + 1:]
    print("Done!")
    return text


def divination(text, old_string, new_string):
    if old_string in text:
        text = text.replace(old_string, new_string)
        print(text)
    return text


def alteration(text, redundant_string):
    if redundant_string in text:
        index_string = text.index(redundant_string)
        text = text[:index_string] + text[index_string + len(redundant_string):]
        print(text)
    return text


spell = input()

command = input()

while command != "Abracadabra":
    command = command.split()
    action = command[0]

    if action == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif action == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif action == "Illusion":
        index, letter = int(command[1]), command[2]
        if 0 <= index < len(spell):
            spell = illusion(spell, index, letter)
        else:
            print("The spell was too weak.")
    elif action == "Divination":
        first_substring, second_substring = command[1], command[2]
        spell = divination(spell, first_substring, second_substring)
    elif action == "Alteration":
        substring = command[1]
        spell = alteration(spell, substring)
    else:
        print("The spell did not work!")

    command = input()

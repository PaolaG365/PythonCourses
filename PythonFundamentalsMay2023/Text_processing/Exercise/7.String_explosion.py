user_string = input()
new_string = ""
explosion_radius = 0

for index in range(len(user_string)):
    if user_string[index] != ">" and explosion_radius > 0:
        explosion_radius -= 1
    elif user_string[index] == ">":
        new_string += ">"
        explosion_radius += int(user_string[index + 1])
    else:
        new_string += user_string[index]

print(new_string)

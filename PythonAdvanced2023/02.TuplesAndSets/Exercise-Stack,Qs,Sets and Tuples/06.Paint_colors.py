from collections import deque

string_to_search = deque(input().split())
colors_found = []
searched_colors = {"red", "yellow", "blue", "orange", "purple", "green"}
colors_needed_to_make_secondaries = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

while string_to_search:
    first_string = string_to_search.popleft()
    second_string = string_to_search.pop() if len(string_to_search) > 0 else ""

    if first_string + second_string in searched_colors:
        colors_found.append(first_string + second_string)
    elif second_string + first_string in searched_colors:
        colors_found.append(second_string + first_string)
    else:
        if len(first_string) > 1:
            string_to_search.insert(len(string_to_search)//2, first_string[:-1])
        if len(second_string) > 1:
            string_to_search.insert(len(string_to_search)//2, second_string[:-1])

for color in set(colors_found):
    if color in colors_needed_to_make_secondaries:
        if not colors_needed_to_make_secondaries[color].issubset(colors_found):
            colors_found.remove(color)

print(colors_found)

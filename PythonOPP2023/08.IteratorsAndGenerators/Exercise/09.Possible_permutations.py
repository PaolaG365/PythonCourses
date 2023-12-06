from itertools import permutations


def possible_permutations(ls_items: list):
    for item in permutations(ls_items):
        yield list(item)


# def possible_permutations(list_to_use: list):
#     if len(list_to_use) <= 1:
#         yield list_to_use
#     else:
#         for (index, element) in enumerate(list_to_use):
#             elements_except_element = list_to_use[:index] + list_to_use[index + 1:]
#             for permutation in possible_permutations(elements_except_element):
#                 yield [element] + permutation


[print(n) for n in possible_permutations([1, 2, 3])]
print()
[print(n) for n in possible_permutations([1])]
print()
[print(n) for n in possible_permutations(["a", "b", "c"])]

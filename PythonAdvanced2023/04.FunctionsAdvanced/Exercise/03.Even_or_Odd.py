operations = {
    "even": lambda x: [el for el in x if el % 2 == 0],
    "odd": lambda x: [el for el in x if el % 2 != 0]
}


def even_odd(*args):
    return operations[args[-1]](args[:-1])


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

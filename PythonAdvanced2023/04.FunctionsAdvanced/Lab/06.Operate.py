from functools import reduce

operations = {
    "+": lambda args: reduce(lambda a, b: a + b, args),
    "-": lambda args: reduce(lambda a, b: a - b, args),
    "*": lambda args: reduce(lambda a, b: a * b, args),
    "/": lambda args: reduce(lambda a, b: a / b, args)
}


def operate(sign, *args):
    return operations[sign](args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 12, 4))
print(operate("-", 5, 1, 1, 1))

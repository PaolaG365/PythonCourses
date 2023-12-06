def type_check(_type):
    def decorator(function):
        def wrapper(*args):

            if not all(isinstance(item, _type) for item in args):
                return "Bad Type"

            return function(*args)

        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2("Not a number"))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter("Hello World"))
print(first_letter(["Not", "A", "String"]))

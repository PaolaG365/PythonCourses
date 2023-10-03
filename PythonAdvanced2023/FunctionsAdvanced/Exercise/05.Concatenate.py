def concatenate(*args, **kwargs):
    result_string = "".join(args)
    for key in kwargs:
        result_string = result_string.replace(key, kwargs[key])

    return result_string


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

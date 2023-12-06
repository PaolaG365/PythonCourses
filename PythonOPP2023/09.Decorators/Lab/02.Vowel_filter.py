def vowel_filter(function):
    def wrapper():
        return [letter for letter in function() if letter in "aeoyiu"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e", "y", "w"]


print(get_letters())

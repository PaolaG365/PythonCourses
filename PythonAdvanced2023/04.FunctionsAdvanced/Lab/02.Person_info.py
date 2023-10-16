def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
info_sample = {"name": "Pesho", "town": "Varna", "age": 22}
print(get_info(**info_sample))

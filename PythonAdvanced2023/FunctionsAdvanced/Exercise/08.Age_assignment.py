def age_assignment(*args, **kwargs):
    name_age = {}
    for name in args:
        name_age[name] = kwargs[name[0]]
    result = []
    for name, age in sorted(name_age.items()):
        result.append(f"{name} is {age} years old.")
    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
def sorting_cheeses(**kwargs):
    for key, value in kwargs.items():
        kwargs[key] = sorted(value, reverse=True)
    sort_cheese = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""
    for k, v in sort_cheese:
        result += f"{k}\n"
        result += '\n'.join(str(el) for el in v)
        result += "\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
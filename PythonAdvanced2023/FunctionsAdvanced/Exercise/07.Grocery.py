def grocery_store(**kwargs):
    # so I was writing the third sorting parameter in the len func... curious...
    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    result = [f"{product}: {quantity}" for product, quantity in sorted_kwargs]
    return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    pasta=2,
    bread=2,
    eggs=20,
    carrot=1,
))

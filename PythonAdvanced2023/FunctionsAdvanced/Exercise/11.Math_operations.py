operations = {
    "a": lambda x, y: x + y,
    "s": lambda x, y: x - y,
    "d": lambda x, y: x / y,
    "m": lambda x, y: x * y,
}


def math_operations(*args, **kwargs):
    counter = 0
    for element_num in range(len(args)):
        counter += 1
        if counter == 4:
            kwargs["m"] = operations["m"](kwargs["m"], args[element_num])
            counter = 0
        elif counter == 3:
            if args[element_num] != 0:
                kwargs["d"] = operations["d"](kwargs["d"], args[element_num])
            else:
                continue
        elif counter == 2:
            kwargs["s"] = operations["s"](kwargs["s"], args[element_num])
        else:
            kwargs["a"] = operations["a"](kwargs["a"], args[element_num])

    sorted_kwargs = sorted(kwargs.items(), key=lambda el: (-el[1], el[0]))
    result = []
    for x, y in sorted_kwargs:
        result.append(f"{x}: {y:.1f}")
    return "\n".join(result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))

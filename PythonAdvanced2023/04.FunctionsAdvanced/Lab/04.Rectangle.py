def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return f"Enter valid values!"

    def area(length, width):
        return f"Rectangle area: {length * width}"

    def perimeter(length, width):
        return f"Rectangle perimeter: {(length + width) * 2}"

    return area(length, width) + f"\n" + perimeter(length, width)


print(rectangle(2, 10))
print(rectangle('2', 10))

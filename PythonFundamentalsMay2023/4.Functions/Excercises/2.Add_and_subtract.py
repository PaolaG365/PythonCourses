def add_subtract(a, b, c):
    def add(a, b): return a + b

    def subtract(c):
        result = add(a, b) - c
        return result

    return subtract(c)


num1, num2, num3 = int(input()), int(input()), int(input())
print(add_subtract(num1, num2, num3))

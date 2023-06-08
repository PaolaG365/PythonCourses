def factorial_division(a, b):  # find factorial of first and second num and divide their result
    factorial_a = a
    factorial_b = b

    for num in range(1, a):
        factorial_a *= num

    for number in range(1, b):
        factorial_b *= number

    result = factorial_a / factorial_b

    return result


num1 = int(input())
num2 = int(input())
print(f"{factorial_division(num1, num2): .2f}")

def perfect_number(n):
    sum_divisors = 0

    for divisor in range(1, int((n / 2) + 1)):
        if n % divisor == 0:
            sum_divisors += divisor

    if sum_divisors == n:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))

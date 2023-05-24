import math
given_number = int(input())


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return print("False")
    return print("True")


is_prime(given_number)

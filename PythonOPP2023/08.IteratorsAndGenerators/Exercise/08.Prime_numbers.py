from math import sqrt


def get_primes(nums: list) -> list:
    for num in nums:
        if num <= 1:
            continue

        for n in range(2, int(sqrt(num)) + 1):
            if num % n == 0:
                break
        else:
            yield num


print(list(get_primes([2, 4, 3, 5, 7, 6, 9, 1, 0])))
print()
print(list(get_primes([100_000_007, -2, 0, 0, 1, 1, 0])))

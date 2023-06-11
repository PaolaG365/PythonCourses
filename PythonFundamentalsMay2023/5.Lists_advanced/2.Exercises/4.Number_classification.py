def positive_negative(numbers):
    positives = []
    negatives = []

    for num in numbers:
        positives.append(num) if num >= 0 else negatives.append(num)

    return positives, negatives


def even_odd(numbers):
    evens = []
    odds = []

    for n in numbers:
        evens.append(n) if n % 2 == 0 else odds.append(n)

    return evens, odds


user_numbers = [int(x) for x in input().split(", ")]
positive_nums, negative_nums = positive_negative(user_numbers)
even_nums, odd_nums = even_odd(user_numbers)

print(f"Positive: {', '.join([str(n) for n in positive_nums])}")
print(f"Negative: {', '.join([str(n1) for n1 in negative_nums])}")
print(f"Even: {', '.join([str(n2) for n2 in even_nums])}")
print(f"Odd: {', '.join([str(n3) for n3 in odd_nums])}")

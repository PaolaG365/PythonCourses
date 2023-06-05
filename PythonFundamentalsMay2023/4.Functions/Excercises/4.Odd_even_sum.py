def odd_even_sum(a=''):
    odd_sum = 0
    even_sum = 0

    for num in a:
        digit = int(num)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    result = f"Odd sum = {odd_sum}, Even sum = {even_sum}"

    return result


number = input()
print(odd_even_sum(number))

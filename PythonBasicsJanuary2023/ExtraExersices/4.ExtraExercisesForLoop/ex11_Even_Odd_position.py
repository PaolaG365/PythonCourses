n = int(input())

odd_maxsize = float('-inf')
odd_minsize = float('inf')
even_maxsize = float('-inf')
even_minsize = float('inf')
odd_sum, even_sum = 0, 0

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        even_sum += number
        if number > even_maxsize:
            even_maxsize = number
        if number < even_minsize:
            even_minsize = number
    else:
        odd_sum += number
        if number > odd_maxsize:
            odd_maxsize = number
        if number < odd_minsize:
            odd_minsize = number

print(f'OddSum={odd_sum:.2f},')
print(f'OddMin=' + ('No,' if odd_minsize == float('inf') else f'{odd_minsize:.2f},'))
print(f'OddMax=' + ('No,' if odd_maxsize == float('-inf') else f'{odd_maxsize:.2f},'))
print(f'EvenSum={even_sum:.2f},')
print(f'EvenMin=' + ('No,' if even_minsize == float('inf') else f'{even_minsize:.2f},'))
print(f'EvenMax=' + ('No' if even_maxsize == float('-inf') else f'{even_maxsize:.2f}'))

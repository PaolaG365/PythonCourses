from math import pi

f = input()
area = 0

if f == 'square':
    a = float(input())
    area = a * a
elif f == 'rectangle':
    a, b = float(input()), float(input())
    area = a * b
elif f == 'circle':
    a = float(input())
    area = pi * (a ** 2)
elif f == 'triangle':
    a, b = float(input()), float(input())
    area = a * b * 0.5

print(f'{area:.3f}')

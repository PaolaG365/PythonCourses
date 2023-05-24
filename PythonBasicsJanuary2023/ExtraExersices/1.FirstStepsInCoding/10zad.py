c = float(input())

if 26.00 <= c <= 35.00:
    print('Hot')
elif 20.1 <= c <= 25.9:
    print('Warm')
elif 15.00 <= c <= 20.00:
    print('Mild')
elif 12.00 <= c <= 14.9:
    print('Cool')
elif 5.00 <= c <= 11.9:
    print('Cold')
else:
    print('unknown')

hour = int(input())
minutes = int(input()) + 15

if minutes > 59:
    hour += 1
    minutes = minutes - 60

if hour >= 24:
    hour -= 24

print(f'{hour}:{minutes:02d}')

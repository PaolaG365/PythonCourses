text = input()

try:
    times_repeated = int(input())
    print(text * times_repeated)
except ValueError:
    print("Variable times must be an integer.")

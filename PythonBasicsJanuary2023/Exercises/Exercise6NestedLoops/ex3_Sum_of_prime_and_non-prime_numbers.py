prime_sum, non_prime_sum = 0, 0

while True:
    n = input()

    if n == "stop":
        break

    number = int(n)

    if number < 0:
        print("Number is negative.")
        continue

    prime_number_checker = True

    for i in range(2, number):
        if (number % i) == 0:
            prime_number_checker = False
            break

    if prime_number_checker:
        prime_sum += number
    else:
        non_prime_sum += number

print(f'Sum of all prime numbers is: {prime_sum}\n'
      f'Sum of all non prime numbers is: {non_prime_sum}')

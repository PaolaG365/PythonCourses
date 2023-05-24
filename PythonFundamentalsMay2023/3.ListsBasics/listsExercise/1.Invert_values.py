num_string = input()
list_of_numbers = num_string.split(" ")
reversed_numbers = []

for num in list_of_numbers:
    reversed_num = int(num) * - 1
    reversed_numbers.append(reversed_num)

print(reversed_numbers)

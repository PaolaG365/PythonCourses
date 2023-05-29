initial_numbers = input().split(", ")
initial_numbers = [int(x) for x in initial_numbers]
zeroes = initial_numbers.count(0)

while 0 in initial_numbers:
    initial_numbers.remove(0)

for num in range(zeroes):
    initial_numbers.append(0)

print(initial_numbers)

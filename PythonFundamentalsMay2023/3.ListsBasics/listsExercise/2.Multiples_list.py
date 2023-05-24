factor = int(input())
count = int(input())
multiples_list = []

while len(multiples_list) < count:
    max_number = factor * count

    for num in range(max_number, 0, - 1):
        if num % factor == 0:
            multiples_list.append(num)

print(sorted(multiples_list))

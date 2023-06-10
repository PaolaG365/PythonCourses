numbers_list = [int(n) for n in input().split(", ")]

print([index for index in range(len(numbers_list)) if numbers_list[index] % 2 == 0])

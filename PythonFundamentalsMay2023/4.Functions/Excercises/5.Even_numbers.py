def even_numbers(n):
    if n % 2 == 0:
        return True
    return False


nums = input().split()
nums = [int(x) for x in nums]
even_nums = list(filter(even_numbers, nums))
print(even_nums)

def min_max_sum(n):
    def min_nums(n): return f"The minimum number is {min(n)}"

    def max_nums(n): return f"The maximum number is {max(n)}"

    def sum_nums(n): return f"The sum number is: {sum(n)}"

    return min_nums(n), max_nums(n), sum_nums(n)


nums = input().split()
nums = [int(x) for x in nums]
print(*min_max_sum(nums), sep="\n")

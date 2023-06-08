def tribonacci_sequence(n):  # n - number of iterations through sequence
    last_three_nums = [0, 1, 1]
    tribonacci_sequence_nums = [1, 1]  # exercise specific

    if n == 1:
        tribonacci_sequence_nums = [1]

    while len(tribonacci_sequence_nums) < n:
        next_num = sum(last_three_nums)
        last_three_nums.pop(0)
        last_three_nums.append(next_num)
        tribonacci_sequence_nums.append(next_num)

    return tribonacci_sequence_nums


number = int(input())
nums_of_sequence = tribonacci_sequence(number)
nums_of_sequence = [str(x) for x in nums_of_sequence]
print(" ".join(nums_of_sequence))

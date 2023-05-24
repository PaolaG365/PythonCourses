nums = [1, 2, 3]

for el in nums:
    print(el)

for el1 in range(len(nums)):
    print(el1)
    if nums[el1] % 2 != 0:
        print(nums[el1], "Hi")

def palindrome_checker(n):
    if n == n[::-1]:
        return True
    return False


nums = input().split(", ")
for num in nums:
    print(palindrome_checker(num))

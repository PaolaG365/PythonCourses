def multiplication_sign(n):  # find what the result will be without multiplying numbers
    negatives_counter = 0
    for num in n:
        if num == 0:
            return "zero"
        elif num < 0:
            negatives_counter += 1
    return "negative" if negatives_counter % 2 != 0 else "positive"


num1 = int(input())
num2 = int(input())
num3 = int(input())
nums_list = [num1, num2, num3]
print(multiplication_sign(nums_list))

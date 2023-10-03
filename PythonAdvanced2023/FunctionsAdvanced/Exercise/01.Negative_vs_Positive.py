def negatives_vs_positives(nums1):
    negatives = 0
    positives = 0
    for num in nums1:
        if int(num) < 0:
            negatives += int(num)
        else:
            positives += int(num)

    result = (f"The {'positives' if abs(positives) > abs(negatives) else 'negatives'} "
              f"are stronger than the "
              f"{'positives' if abs(positives) < abs(negatives) else 'negatives'}")

    return f"{negatives}\n{positives}\n{result}"


nums = input().split()
print(negatives_vs_positives(nums))

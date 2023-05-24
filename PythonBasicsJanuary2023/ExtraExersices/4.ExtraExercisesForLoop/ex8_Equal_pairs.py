n = int(input())

max_diff = float('-inf')
last_sum = float('-inf')

for i in range(n):
    n1, n2 = int(input()), int(input())
    current_sum = n1 + n2

    if i == 0:
        last_sum = n1 + n2
        continue

    if last_sum != current_sum:
        if abs(current_sum - last_sum) > max_diff:
            max_diff = abs(current_sum - last_sum)
    last_sum = n1 + n2

print(f'Yes, value={last_sum}'if max_diff == float('-inf')
      else f'No, maxdiff={max_diff}')

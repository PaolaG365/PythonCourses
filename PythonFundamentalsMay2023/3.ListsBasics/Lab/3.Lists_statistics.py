number_of_lines = int(input())
positive_numbers = []
negative_numbers = []

for n in range(number_of_lines):
    number = int(input())
    if number < 0:
        negative_numbers.append(number)
    else:
        positive_numbers.append(number)

print(f"{positive_numbers}\n{negative_numbers}")
print(f"Count of positives: {len(positive_numbers)}\nSum of negatives: {sum(negative_numbers)}")

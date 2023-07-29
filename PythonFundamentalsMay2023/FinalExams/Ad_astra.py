import re

diet_pattern = re.compile(r"(?P<sep>[#|])(?P<item_name>[A-Za-z ]+)(?P=sep)"
                          r"(?P<exp_date>\d{2}/\d{2}/\d{2})(?P=sep)"
                          r"(?P<calories>\d+)(?P=sep)")

diet_info = []

text = input()
data = re.finditer(diet_pattern, text)
total_calories = 0

for info in data:
    diet_info.append({'item_name': info['item_name'],
                      'exp_date': info['exp_date'],
                      'calories': info['calories']})
    total_calories += int(info['calories'])

print(f"You have food to last you for: {total_calories//2000} days!")
for collected_data in diet_info:
    print(f"Item: {collected_data['item_name']},"
          f" Best before: {collected_data['exp_date']},"
          f" Nutrition: {collected_data['calories']}")

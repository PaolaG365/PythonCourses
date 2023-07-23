import re

phone_number_pattern = re.compile(r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b")

text = input()
phone_matches = re.findall(phone_number_pattern, text)
print(*phone_matches, sep=", ")

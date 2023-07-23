import re
input_lines = int(input())

for _ in range(input_lines):
    text = input()
    name = re.search(r"@[a-z]+\|", text, re.IGNORECASE)
    age = re.search(r"#\d+\*", text)
    print(f"{name.group().strip('@|')} is {age.group().strip('#*')} years old.")

import re

lines = []

while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

text = "\n".join(lines)

valid_pattern = re.findall(r"\d+", text)
print(" ".join(valid_pattern))

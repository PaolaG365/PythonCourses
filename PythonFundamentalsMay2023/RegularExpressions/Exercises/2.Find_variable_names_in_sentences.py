import re

sentence = input()

valid_names = re.findall(r"\b_([A-Za-z0-9]+)\b", sentence)

print(",".join(valid_names))

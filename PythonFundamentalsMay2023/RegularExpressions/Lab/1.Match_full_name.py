import re

name_pattern = re.compile(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b")
text_to_search = input()

found_names = re.findall(name_pattern, text_to_search)
print(" ".join(found_names))

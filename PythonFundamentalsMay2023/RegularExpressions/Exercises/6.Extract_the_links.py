import re

pattern = r"w{3}\.[A-Za-z0-9-\.]+\.[a-z]+"
text = input()
links = []

while text:
    site_match = re.search(pattern, text)
    if site_match:
        links.append(site_match.group())

    text = input()

print(*links, sep="\n")

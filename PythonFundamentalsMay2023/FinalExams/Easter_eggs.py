# import re
#
# egg_info_pattern = re.compile(r"[@#]+(?P<egg_colour>[a-z]{3,})[@#]+"
#                               r"[^A-Za-z0-9]*/+(?P<eggs_amount>\d+)/+")
#
# sample_text = input()
#
# valid_egg_info = re.finditer(egg_info_pattern, sample_text)
#
# for egg_info in valid_egg_info:
#     print(f"You found {egg_info.group('eggs_amount')} {egg_info.group('egg_colour')} eggs!")
import re

text = input()

pattern = r'[#@]+([a-z]{3,})[@#]+[^A-Za-z0-9]*\/(\d+)\/'

matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)

for match in matches:
    color = match[0]
    amount = match[1]
    print(f"You found {amount} {color} eggs!")

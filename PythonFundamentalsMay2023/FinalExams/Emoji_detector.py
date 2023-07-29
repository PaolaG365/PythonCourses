import re

coolness_pattern = re.compile(r"\d")
valid_emoji_pattern = re.compile(r"(?P<sep>:{2}|\*{2})(?P<emoji>[A-Z][a-z]{2,})(?P=sep)")

text = input()

coolness_threshold = 1
for number in re.finditer(coolness_pattern, text):
    coolness_threshold *= int(number.group())

emojis = re.finditer(valid_emoji_pattern, text)
counter = 0
cool_emojis = []

for emoji in emojis:
    emoji_coolness = 0
    counter += 1
    for char in emoji.group('emoji'):
        emoji_coolness += ord(char)
    if emoji_coolness > coolness_threshold:
        cool_emojis.append(f"{emoji.group('sep')}{emoji.group('emoji')}{emoji.group('sep')}")

print(f"Cool threshold: {coolness_threshold}")
print(f"{counter} emojis found in the text. The cool ones are:")
print(*cool_emojis, sep="\n")

import re

demons_list = [text.strip() for text in input().split(",")]
demon_book = []

health_demon_pattern = re.compile(r"[^0-9+\-*/.]")
damage_demon_pattern = re.compile(r"[+-]?\d+[.\d]*")
additional_damage_amplifiers = re.compile(r"[*/]")

for demon_entry in demons_list:
    demon_health = sum(ord(char) for char in re.findall(health_demon_pattern, demon_entry)) # returns list
    sum_base_dmg = sum(float(num) for num in re.findall(damage_demon_pattern, demon_entry))
    damage_amplifiers = re.findall(additional_damage_amplifiers, demon_entry)

    if damage_amplifiers and sum_base_dmg:
        for amplifier in damage_amplifiers:
            if amplifier == "/":
                sum_base_dmg = sum_base_dmg / 2
            else:
                sum_base_dmg = sum_base_dmg * 2

    demon_book.append({"name": demon_entry, "health": demon_health, "damage": sum_base_dmg})

for demon in sorted(demon_book, key=lambda x: x["name"]):
    print(f"{demon['name']} - {demon['health']} health, {demon['damage']:.2f} damage")

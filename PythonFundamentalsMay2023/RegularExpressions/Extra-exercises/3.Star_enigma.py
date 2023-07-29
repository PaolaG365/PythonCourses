import re

decoded_message_pattern = re.compile(r"@(?P<planet_name>[A-Za-z]+)[^@\-!:>]*"
                                     r":(?P<population>\d+)[^@\-!:>]*"
                                     r"!(?P<attack_type>[AD])![^@\-!:>]*"
                                     r"->(?P<souldiers>\d+)")

messages = int(input())
attack_type = {"A": "Attacked", "D": "Destroyed"}
planets_event = {"Attacked": [], "Destroyed": []}

for data in range(messages):
    message = input()
    sum_special_chars = sum(message.lower().count(letter) for letter in "star")
    decoded_message = ""
    for symbol in message:
        decoded_message += chr(ord(symbol) - sum_special_chars)

    event_planet = re.search(decoded_message_pattern, decoded_message)
    if event_planet:
        planets_event[attack_type[event_planet.group('attack_type')]].append(event_planet.group('planet_name'))

for event, planets in planets_event.items():
    print(f"{event} planets: {len(planets)}")
    if planets:
        planets = sorted(planets)
        [print(f"-> {planet}") for planet in planets]

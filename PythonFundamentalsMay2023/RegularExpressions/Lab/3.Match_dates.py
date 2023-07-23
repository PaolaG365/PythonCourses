import re

date_pattern = re.compile(r"\b(?P<day>\d{2})(?P<sep>[.\-/])"
                          r"(?P<month>[A-Z][a-z]{2})(?P=sep)"
                          r"(?P<year>\d{4})\b")

dates = input()
valid_dates = re.finditer(date_pattern, dates)

for date in valid_dates:
    print(f"Day: {date['day']}, Month: {date['month']}, Year: {date['year']}")

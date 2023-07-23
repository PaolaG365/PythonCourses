import re

valid_email_pattern_in_your_dreams_and_hopes = re.compile(r"\s(([a-z0-9]+[a-z0-9.\-_]*)@"
                                                          r"([a-z\-]+)(\.[a-z]+)+)\b")

text_to_search_for_hope = input()
valid_like_hell_emails = re.findall(valid_email_pattern_in_your_dreams_and_hopes, text_to_search_for_hope)

for a_maybe_valid_email in valid_like_hell_emails:
    print(a_maybe_valid_email[0])

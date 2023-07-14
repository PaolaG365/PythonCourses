# validate length
def valid_length(mail): return True if 3 <= len(mail) <= 16 else False


# check if email is letter, digit or special symbols (-_)
def valid_chars(mail): return True if (mail.isalnum() or "-" in mail or "_" in mail) else False


# no whitespaces in email name
def no_whitespaces(mail): return True if " " not in mail else False


def is_valid_email(mail):
    if valid_length(mail) and valid_chars(mail) and no_whitespaces(mail):
        return True
    return False


email_names_list = input().split(", ")
valid_emails = []

for email in email_names_list:
    if is_valid_email(email):
        valid_emails.append(email)

print(*valid_emails, sep="\n")

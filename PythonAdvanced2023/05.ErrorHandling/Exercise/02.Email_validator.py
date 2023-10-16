# freestyling it a little

class NameTooShortError(Exception):
    def __init__(self, sample_email):
        self.sample_email = sample_email
        super().__init__(f"Your email: {sample_email}. Username must be more than 4 characters")  # returns error msg


class MustContainAtSymbolError(Exception):
    def __init__(self, sample_email):
        self.sample_email = sample_email
        super().__init__(f"Your email: {sample_email}. Email must contain @")


class InvalidDomainError(Exception):
    def __init__(self, user_domain):
        self.user_domain = user_domain
        super().__init__(f"Your domain: .{user_domain}. Domain must be one of the following: .com, .bg, .org, .net")


USERNAME_MIN_LENGTH = 5
ALLOWED_DOMAINS = ["com", "bg", "org", "net"]


def email_validator(user_email):

    if "@" not in user_email:
        raise MustContainAtSymbolError(user_email)

    elif len(user_email.split("@")[0]) < USERNAME_MIN_LENGTH:
        raise NameTooShortError(user_email)

    elif user_email.split(".")[-1] not in ALLOWED_DOMAINS:
        raise InvalidDomainError(user_email.split(".")[-1])

    return "Email is valid"


while True:
    print(email_validator(input("Enter your email: ")))


# class NameTooShortError(Exception):
#     pass
#
#
# class MustContainAtSymbolError(Exception):
#     pass
#
#
# class InvalidDomainError(Exception):
#     pass
#
#
# def email_validator(user_email):
#     valid_username_length_min = 5
#     allowed_domains = ["com", "bg", "org", "net"]
#
#     if "@" not in user_email:
#         raise MustContainAtSymbolError("Email must contain @")
#
#     elif len(user_email.split("@")[0]) < valid_username_length_min:
#         raise NameTooShortError("Name must be more than 4 characters")
#
#     elif user_email.split(".")[-1] not in allowed_domains:
#         raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
#
#     return "Email is valid"
#
#
# while True:
#     print(email_validator(input()))

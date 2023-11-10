class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, username: str):
        return len(username) >= self.min_length

    def __is_mail_valid(self, mail: str):
        return mail in self.mails

    def __is_domain_valid(self, domain: str):
        return domain in self.domains

    def validate(self, email: str):
        username, data = email.split('@')
        mail = data.split(".")[0]
        domain = ".".join(data.split(".")[1:])
        return self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg", "co.uk"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("pe77er@gmail.co.uk"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

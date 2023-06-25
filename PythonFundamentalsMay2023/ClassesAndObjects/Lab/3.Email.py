class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def sent(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()

while command != "Stop":
    command = command.split()
    email_sender = command[0]
    email_receiver = command[1]
    email_content = command[2]
    user_email = Email(email_sender, email_receiver, email_content)
    emails.append(user_email)

    command = input()

sent_emails = [int(x) for x in input().split(", ")]

for num in sent_emails:
    emails[num].sent()

for email in emails:
    print(email.get_info())

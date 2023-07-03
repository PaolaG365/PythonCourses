users_submissions = {}
language_submissions_counter = {}

command = input()

while command != "exam finished":
    command = command.split("-")
    username, language = command[0], command[1]

    if language != "banned":
        points = int(command[2])
        if language not in language_submissions_counter:
            language_submissions_counter[language] = 0
        language_submissions_counter[language] += 1
        if username not in users_submissions:
            users_submissions[username] = 0
        if points > users_submissions[username]:
            users_submissions[username] = points

    elif language == "banned":
        del users_submissions[username]

    command = input()

print("Results:")
[print(f"{user} | {user_result}") for user, user_result in users_submissions.items()]
print("Submissions:")
[print(f"{lang} - {count}") for lang, count in language_submissions_counter.items()]

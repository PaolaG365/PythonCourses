contests_and_passwords = {}
participants_scores = {}

contest_and_pass = input()

while contest_and_pass != "end of contests":
    contest, password = contest_and_pass.split(":")
    if contest not in contests_and_passwords:
        contests_and_passwords[contest] = ""
    contests_and_passwords[contest] = password
    contest_and_pass = input()

user_input = input()

while user_input != "end of submissions":
    user_input = user_input.split("=>")
    participant_contest, participant_pass = user_input[0], user_input[1]
    username, user_score = user_input[2], int(user_input[3])
    if participant_contest in contests_and_passwords:
        if participant_pass == contests_and_passwords[participant_contest]:
            if username not in participants_scores:
                participants_scores[username] = {}
                participants_scores[username].update({participant_contest: user_score})
            else:
                if participant_contest in participants_scores[username]:
                    if user_score > participants_scores[username][participant_contest]:
                        participants_scores[username][participant_contest] = user_score
                else:
                    participants_scores[username].update({participant_contest: user_score})

    user_input = input()


#  get best participant
max_score_student = ""
max_score = 0
for human, score in participants_scores.items():
    total_score_student = sum(participants_scores[human].values())
    if total_score_student > max_score:
        max_score_student = human
        max_score = total_score_student

print(f"Best candidate is {max_score_student} with total {max_score} points.")

# prints students with their scores in descending order
print("Ranking:")
for participant in sorted(participants_scores.keys()):
    print(participant)
    sorted_scores = sorted(participants_scores[participant].items(), key=lambda x: x[1], reverse=True)
    scores_sorted = dict(sorted_scores)
    for key, value in scores_sorted.items():
        print(f"#  {key} -> {value}")

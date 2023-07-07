courses_participants_ranking = {}
individual_ranking = {}

command = input()

while command != "no more time":
    command = command.split(" -> ")
    username, contest, points = command[0], command[1], int(command[2])
    if contest not in courses_participants_ranking:
        courses_participants_ranking[contest] = {username: points}
    elif username not in courses_participants_ranking[contest]:
        courses_participants_ranking[contest].update({username: points})
    elif points > courses_participants_ranking[contest][username]:
        courses_participants_ranking[contest][username] = points
    command = input()

# get total points by student
for contest, student_score in courses_participants_ranking.items():
    for student, score in student_score.items():
        if student not in individual_ranking:
            individual_ranking[student] = 0
        individual_ranking[student] += score

# sorting dictionaries by scores and alphabetically by name

for contest, student in courses_participants_ranking.items():
    print(f"{contest}: {len(student)} participants")
    sorted_students = sorted(student.items(), key=lambda x: (-x[1], x))
    rank = 1
    for student_name, score in sorted_students:
        print(f"{rank}. {student_name} <::> {score}")
        rank += 1

sorted_individual_ranking = sorted(individual_ranking.items(), key=lambda x: (-x[1], x))
print("Individual standings:")
rank = 1
for individual, total_score in sorted_individual_ranking:
    print(f"{rank}. {individual} -> {total_score}")
    rank += 1

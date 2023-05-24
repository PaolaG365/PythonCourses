student_tickets, standard_tickets, kid_tickets = 0, 0, 0
total_tickets = 0

while True:
    movie_name = input()

    if movie_name == "Finish":
        break

    free_space = int(input())
    counter = 0

    for _ in range(free_space):
        ticket_type = input()

        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        counter += 1
        total_tickets += 1

    print(f'{movie_name} - {counter / free_space * 100:.2f}% full.')

print(f'Total tickets: {total_tickets}\n{student_tickets / total_tickets * 100:.2f}% student tickets.\n'
      f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.\n'
      f'{kid_tickets / total_tickets * 100:.2f}% kids tickets.')

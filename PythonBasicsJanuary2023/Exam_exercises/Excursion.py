number_people, hotel = int(input()), int(input())
transport_tickets, museum_tickets = int(input()), int(input())

hotel_one_person = hotel * 20
transport_one_person = transport_tickets * 1.60
museum_one_person = museum_tickets * 6

total_one_person = hotel_one_person + transport_one_person + museum_one_person

total_group = total_one_person * number_people
total_with_unexpected_expenses = total_group * 1.25

print(f"{total_with_unexpected_expenses:.2f}")

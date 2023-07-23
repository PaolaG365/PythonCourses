def winning_ticket(ticket_to_check):
    if len(ticket_to_check) != 20:
        return "invalid ticket"
    winning_symbols = ["@", '#', '$', '^']
    first_side = ticket_to_check[:10]
    second_side = ticket_to_check[10:]
    for symbol in winning_symbols:
        for count in range(10, 5, -1):
            symbols_to_match = symbol * count
            if symbols_to_match in first_side and symbols_to_match in second_side:
                if count == 10:
                    return f'ticket "{ticket_to_check}" - {count}{symbol} Jackpot!'
                return f'ticket "{ticket_to_check}" - {count}{symbol}'
    return f'ticket "{ticket_to_check}" - no match'


tickets_to_check = [lottery_ticket.strip() for lottery_ticket in input().split(", ")]

for ticket in tickets_to_check:
    print(winning_ticket(ticket))

import re

tickets = input().split(",")
winning_symbols = ["@", "#", "$", "^"]


def longest_run(symbol, half):
    return max((len(run) for run in re.findall(re.escape(symbol) + "+", half)), default=0)


for ticket in tickets:
    ticket = ticket.strip()
    if len(ticket) != 20:
        print(f"invalid ticket")
        continue

    is_found = False
    left_h, right_h = ticket[:10], ticket[10:]
    for s in winning_symbols:
        s_length = min(longest_run(s, left_h), longest_run(s, right_h))
        if s_length == 10:
            print(f'ticket "{ticket}" - 10{s} Jackpot!')
            is_found = True
            break

        elif s_length >= 6:
            print(f'ticket "{ticket}" - {s_length}{s}')
            is_found = True
            break

    if not is_found:
        print(f'ticket "{ticket}" - no match')

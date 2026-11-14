def add_player(pl, pos, sk, pool):
    sk = int(sk)
    if pl not in pool:
        pool[pl] = {}
    
    if pos not in pool[pl] or pool[pl][pos] < sk:
        pool[pl][pos] = sk
    
    return pool


def fight(pl1, pl2, pool):
    if pool[pl1].keys() & pool[pl2].keys():
        pl1_total, pl2_total = sum(pool[pl1].values()), sum(pool[pl2].values())
        if pl1_total < pl2_total:
            del pool[pl1]
        elif pl2_total < pl1_total:
            del pool[pl2]

    return pool


command, players_pool = input(), {}
while command != "Season end":
    if " vs " in command:
        player1, player2 = command.split(" vs ")
        if player1 in players_pool and player2 in players_pool:
            players_pool = fight(player1, player2, players_pool)
    else:
        player, position, skill = command.split(" -> ")
        players_pool = add_player(player, position, skill, players_pool)

    command = input()

for ple, items in sorted(players_pool.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{ple}: {sum(items.values())} skill")
    for ple2, s in sorted(items.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {ple2} <::> {s}")

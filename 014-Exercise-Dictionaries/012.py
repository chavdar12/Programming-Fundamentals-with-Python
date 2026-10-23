contests_passwords, contests = {}, {}
command = input()
while command != "end of contests":
    contest, password = command.split(":")
    contests_passwords[contest] = password
    command = input()

command = input()
while command != "end of submissions":
    contest, password, username, points = command.split("=>")
    points = int(points)
    if contest not in contests_passwords or password != contests_passwords[contest]:
        command = input()
        continue

    if username not in contests:
        contests[username] = {}
    
    if contest not in contests[username] or contests[username][contest] < points:
        contests[username][contest] = points
    
    command = input()

best_candidate, best_contests = max(contests.items(), key=lambda x: sum(x[1].values()))
print(f"Best candidate is {best_candidate} with total {sum(best_contests.values())} points.\nRanking:")
for u, contests_data in sorted(contests.items()):
    print(u)
    for l, p in sorted(contests_data.items(), key=lambda x: -x[1]):
        print(f"#  {l} -> {p}")

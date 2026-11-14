MAX_HP, MAX_MP = 100, 200

heroes = {}
for _ in range(int(input())):
    name, hp, mp = input().split()
    heroes[name] = {"hp": int(hp), "mp": int(mp)}

command = input()
while command != "End":
    action, name, *args = command.split(" - ")
    hero = heroes[name]
    if action == "CastSpell":
        needed, spell = int(args[0]), args[1]
        if hero["mp"] >= needed:
            hero["mp"] -= needed
            print(f"{name} has successfully cast {spell} and now has {hero['mp']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell}!")
    elif action == "TakeDamage":
        damage, attacker = int(args[0]), args[1]
        hero["hp"] -= damage
        if hero["hp"] > 0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {hero['hp']} HP left!")
        else:
            del heroes[name]
            print(f"{name} has been killed by {attacker}!")
    elif action == "Recharge":
        recovered = min(int(args[0]), MAX_MP - hero["mp"])
        hero["mp"] += recovered
        print(f"{name} recharged for {recovered} MP!")
    elif action == "Heal":
        recovered = min(int(args[0]), MAX_HP - hero["hp"])
        hero["hp"] += recovered
        print(f"{name} healed for {recovered} HP!")
    command = input()

for name, stats in heroes.items():
    print(name)
    print(f"  HP: {stats['hp']}")
    print(f"  MP: {stats['mp']}")

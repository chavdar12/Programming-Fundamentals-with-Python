towns = {}

line = input()
while line != "Sail":
    town, people, gold = line.split("||")
    stats = towns.setdefault(town, {"people": 0, "gold": 0})
    stats["people"] += int(people)
    stats["gold"] += int(gold)
    line = input()

line = input()
while line != "End":
    action, town, *args = line.split("=>")
    if action == "Plunder":
        people, gold = int(args[0]), int(args[1])
        towns[town]["people"] -= people
        towns[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if towns[town]["people"] <= 0 or towns[town]["gold"] <= 0:
            del towns[town]
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        gold = int(args[0])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            towns[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {towns[town]['gold']} gold.")
    line = input()

if towns:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    for town, stats in towns.items():
        print(f"{town} -> Population: {stats['people']} citizens, Gold: {stats['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

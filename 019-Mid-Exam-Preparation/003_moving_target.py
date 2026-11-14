targets = [int(x) for x in input().split()]

command = input()
while command != "End":
    action, index, value = command.split()
    index, value = int(index), int(value)
    if action == "Shoot" and 0 <= index < len(targets):
        targets[index] -= value
        if targets[index] <= 0:
            targets.pop(index)
    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if 0 <= index - value and index + value < len(targets):
            del targets[index - value:index + value + 1]
        else:
            print("Strike missed!")
    command = input()

print("|".join(map(str, targets)))

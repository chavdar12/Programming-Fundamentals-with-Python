numbers = [int(x) for x in input().split()]

command = input()
while command != "end":
    action, *indexes = command.split()
    if action == "swap":
        a, b = map(int, indexes)
        numbers[a], numbers[b] = numbers[b], numbers[a]
    elif action == "multiply":
        a, b = map(int, indexes)
        numbers[a] *= numbers[b]
    elif action == "decrease":
        numbers = [n - 1 for n in numbers]
    command = input()

print(", ".join(map(str, numbers)))

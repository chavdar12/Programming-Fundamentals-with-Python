stops = input()

command = input()
while command != "Travel":
    action, *args = command.split(":")
    if action == "Add Stop":
        index = int(args[0])
        if 0 <= index < len(stops):
            stops = stops[:index] + args[1] + stops[index:]
    elif action == "Remove Stop":
        start, end = int(args[0]), int(args[1])
        if 0 <= start <= end < len(stops):
            stops = stops[:start] + stops[end + 1:]
    elif action == "Switch":
        stops = stops.replace(args[0], args[1])
    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")

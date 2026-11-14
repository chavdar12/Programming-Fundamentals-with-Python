message = input()

command = input()
while command != "Decode":
    action, *args = command.split("|")
    if action == "Move":
        n = int(args[0])
        message = message[n:] + message[:n]
    elif action == "Insert":
        index = int(args[0])
        message = message[:index] + args[1] + message[index:]
    elif action == "ChangeAll":
        message = message.replace(args[0], args[1])
    command = input()

print(f"The decrypted message is: {message}")

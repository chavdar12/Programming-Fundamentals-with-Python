total = 0
command = input()
while command not in ("special", "regular"):
    price = float(command)
    if price <= 0:
        print("Invalid price!")
    else:
        total += price
    command = input()

if total == 0:
    print("Invalid order!")
else:
    taxes = total * 0.2
    final = (total + taxes) * (0.9 if command == "special" else 1)
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {final:.2f}$")

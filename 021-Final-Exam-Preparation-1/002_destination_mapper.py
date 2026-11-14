import re

destinations = [m.group(2) for m in re.finditer(r"([=/])([A-Z][A-Za-z]{2,})\1", input())]
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {sum(map(len, destinations))}")

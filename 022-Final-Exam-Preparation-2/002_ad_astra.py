import re

DAILY_CALORIES = 2000

items = re.findall(r"([#|])([A-Za-z ]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1", input())
calories = sum(int(item[3]) for item in items)

print(f"You have food to last you for: {calories // DAILY_CALORIES} days!")
for _, name, date, nutrition in items:
    print(f"Item: {name}, Best before: {date}, Nutrition: {nutrition}")

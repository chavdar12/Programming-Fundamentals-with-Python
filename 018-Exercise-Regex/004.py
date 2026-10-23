import re

text = input()
pattern = f"\\b{re.escape(input())}\\b"
matches = re.findall(pattern, text, re.IGNORECASE)
print(len(matches))

string = input().lower()
print(sum(string.count(word) for word in ["sand", "water", "fish", "sun"]))

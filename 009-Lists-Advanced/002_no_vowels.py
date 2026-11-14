vowels = ["a", "o", "u", "e", "i"]
print(''.join(let for let in input() if let.lower() not in vowels))

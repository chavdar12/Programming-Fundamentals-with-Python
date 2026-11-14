number = int(input())
digit = int(input())

count = 0
while number:
    count += (number & 1) == digit
    number >>= 1
print(count)

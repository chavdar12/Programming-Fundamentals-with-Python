result = 0
for number in map(int, input().split()):
    result ^= number
print(result)

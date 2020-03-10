import math
a, b = map(int, input().split())

for i in range(1,10 ** 6):
    asub = math.floor(i * 0.08)
    bsub = math.floor(i * 0.1)
    if asub == a and bsub == b:
        print(i)
        exit()

print("-1")

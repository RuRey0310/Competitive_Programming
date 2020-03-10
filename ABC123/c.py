import math
n = int(input())
man = [int(input()) for i in range(5)]

min1 = float("inf")
for i in range(5):
    min1 = min(min1, man[i])
ans = math.ceil(n / min1)
print(ans+4)

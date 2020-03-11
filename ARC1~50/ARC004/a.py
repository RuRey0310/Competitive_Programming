import math

n = int(input())
x, y= [0] * n, [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        leng = math.sqrt(pow(x[i] - x[j], 2) + pow(y[i] - y[j], 2))
        ans = max(ans, leng)

print(ans)

from math import factorial
n,m = map(int, input().split())

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        ans += 1

for i in range(m - 1):
    for j in range(i + 1, m):
        ans += 1

print(ans)
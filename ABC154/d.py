n,k = map(int, input().split())
p = list(map(int, input().split()))

saikoro = [0] * 1001
for i in range(1, 1001):
    saikoro[i] = (saikoro[i-1] + i)

s = [0] * (n + 1)
for u in range(1,n + 1):
    s[u] = saikoro[p[u - 1]] / p[u - 1] + s[u - 1]

ans = 0
for j in range(k - 1,n):
    ans = max(ans, s[j + 1] - s[j + 1 - k])
 
print(ans)

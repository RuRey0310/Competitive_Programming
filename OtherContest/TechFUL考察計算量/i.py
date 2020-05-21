n = int(input())
d = list(map(int, input().split()))
m = int(input())
c, k = [0] * m, [0] * m
a = [0] * m
for i in range(m):
    s = list(map(int, input().split()))
    c[i] = s[0]
    k[i] = s[1]
    for j in range(2, len(s)):
        a[i] += 2 ** (s[j] - 1)

INF = 10 ** 9
dp = [[INF] * (2 ** n + 1) for i in range(m + 1)]
dp[0][0] = 0
for i in range(m):
    for j in range(2 ** n):
        if dp[i][j] != INF:
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
            sub = j ^ a[i]
            dp[i + 1][sub] = min(dp[i + 1][sub], dp[i][j] + c[i])

cost = [0] * (2 ** n)
for i in range(2 ** n):
    tf = [False] * n
    for j in range(n):
        if((i >> j) & 1):
            tf[j] = True
    
    for j in range(n):
        if tf[j]:
            cost[i] += d[j]
    
ans = 0
for i in range(m + 1):
    for j in range(2 ** n):
        if dp[i][j] != INF:
            ans = max(ans,cost[j] - dp[i][j])
print(ans)
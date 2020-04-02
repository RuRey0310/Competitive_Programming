n = int(input())
p = list(map(int, input().split()))

dp = [[False] * 10001 for i in range(n + 1)]
dp[0][0] = True
for i in range(1, n + 1):
    for j in range(10001):
        if j - p[i - 1] >= 0:
            if dp[i - 1][j - p[i - 1]]:
                dp[i][j] = True
        if dp[i - 1][j]:
            dp[i][j] = True

ans = 0
for i in range(10001):
    if dp[n][i]:
        ans += 1

print(ans)
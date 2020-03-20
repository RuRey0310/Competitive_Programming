n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0] * (k + 10) for i in range(n + 10)]

for i in range(n):
    for j in range(k):
        if j - a[i] == 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - a[i]] + 1)
        if j - a[i] >= 0:
            if dp[i][j - a[i]] != 0:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - a[i]] + 1)
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

ans = 0
for i in range(n + 10):
    for j in range(k + 10):
        if dp[i][j] != 0:
            ans = max(ans, b[j - 1] + c[dp[i][j] - 1])

print(ans)
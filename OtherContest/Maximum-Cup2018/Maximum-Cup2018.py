n, m, l, x = map(int, input().split())
a = list(map(int, input().split()))

INF = float("inf")
dp = [[INF] * (m + 1) for i in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    if a[i] <= m:
        dp[i + 1][a[i]] = 1
    else:
        dp[i + 1][a[i] % m] = a[i] // m
    for j in range(m):
        if dp[i][j] == 1:
            if j + a[i] <= m:
                dp[i + 1][j + a[i]] = dp[i][j]
            else:
                dp[i + 1][(j + a[i]) % m] = min(dp[i + 1][(j + a[i]) % m], dp[i][j] + ((j + a[i]) // m))
        dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j + 1])

if dp[n][l] <= x:
    print("Yes")
else:
    print("No")
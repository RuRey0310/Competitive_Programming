import math
n, k = map(int, input().split())
a = [int(input()) for i in range(n)]

dp = [[0] * (k + 1) for i in range(n + 1)]
for i in range(n):
    for j in range(k):
        if i == 0:
            rate = 0
        else:
            rate = dp[i][j] / a[i - 1]
        if rate == 0:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            if i == j:
                dp[i + 1][j + 1] = dp[i][j] + math.ceil((a[i - 1] * rate) + 1)
            else:
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i][j] + math.ceil((a[i - 1] * rate) + 1))


ans = 0
for i in range(k):
    if dp[n][i] <= k:
        ans = max(ans, i)
    else:
        break

print(ans)
n, k = map(int, input().split())
a = [int(input()) for i in range(n)]

dp = [[31] * (k + 1) for i in range(n + 1)]
summ = 0
dp[0][0] = 0
for i in range(n):
    if i == 0:
        dp[1][1] = 1
        dp[1][0] = 0
    else:
        for j in range(i + 1):
            rate = dp[i][j] * a[i]
            rate = (rate // summ) + 1
            if rate <= a[i]:
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + rate)
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    summ += a[i]

ans = 0
for i in range(n,0,-1):
    if dp[-1][i] <= k:
        ans = i
        break

if summ == 0:
    ans = 0
elif summ == k:
    ans = 1

print(ans)
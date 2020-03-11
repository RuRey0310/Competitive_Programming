h, n = map(int, input().split())
a, b= [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

max_v = 10100
x = float("inf")

dp = [x] * max_v

dp[0] = 0
for i in range(1,max_v):
    for j in range(n):
        dp[i] = min(dp[i], dp[i - a[j]] + b[j])

ans = x
for i in range(max_v):
    if i >= h:
        ans = min(ans, dp[i])

print(ans)

n,m = map(int,input().split())
breaks = [0] * (n + 1)
for i in range(m):
    a = int(input())
    breaks[a] = 1

mod = (10**9)+7
dp = [0] * (n + 1)
dp[n] = 1
for i in reversed(range(n)):
    if(breaks[i] == 1):
        dp[i] = 0
        continue
    if(i == n - 1):
        dp[i] = dp[i+1]
    else:
        dp[i] = dp[i+1] + dp[i+2]
print(dp[0] % mod)

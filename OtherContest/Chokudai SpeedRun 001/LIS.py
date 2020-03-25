import bisect
n = int(input())
a = list(map(int, input().split()))

INF = float("inf")
dp = [INF] * (n + 1)
dp[0] = a[0]
length = 1
for i in range(1,n):
    if dp[length - 1] < a[i]:
        dp[length] = a[i]
        length += 1
    else:
        ind = bisect.bisect_left(dp, a[i], 0, length)
        dp[ind] = a[i]

print(length)
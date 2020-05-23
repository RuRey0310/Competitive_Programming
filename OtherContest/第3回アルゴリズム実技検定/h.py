n, l = map(int, input().split())
x = list(map(int, input().split()))
t1, t2, t3 = map(int, input().split())

INF = 10 ** 9
dp = [INF] * (l + 5)
cnt = 0
dp[0] = 0
move1 = INF
move2 = INF
move3 = INF
ans = INF
for i in range(1, l + 4):
    if i > l:
        g = dp[i - 2] + t1 // 2 + t2 // 2
        gg = dp[i - 4] + t1 // 2 + t2 * (3.5 - (i - l))
        gg = int(gg)
        ans = min(ans,g, gg)
    if x[cnt] == i:
        move1 = t3 + t1 + dp[i - 1]
    else:
        move1 = t1 + dp[i - 1]
    if i > 1:
        if x[cnt] == i:
            move2 = t1 + t3 + t2 + dp[i - 2]
        else:
            move2 = t1 + t2 + dp[i - 2]
    if i > 3:
        if x[cnt] == i:
            move3 = t1 + t3 + t2 * 3 + dp[i - 4]
        else:
            move3 = t1 + t2 * 3 + dp[i - 4]
    dp[i] = min(move1, move2, move3, dp[i])
    if x[cnt] == i:
        cnt += 1
        cnt = min(cnt,n - 1)

print(min(dp[l],ans))
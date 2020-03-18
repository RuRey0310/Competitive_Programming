s = list(input())
n = int(input())
lr = [list(map(int, list(input().split()))) for i in range(n)]

lr.sort(key = lambda x: x[0])

dp = [-1] * len(s)
cnt = 0
for i in range(n):
    if dp[lr[i][0] - 1] != -1:
        dp[lr[i][0] - 1] = -1
        cnt -= 1
    else:
        dp[lr[i][0] - 1] = cnt
    if dp[lr[i][1] - 1] != -1:
        dp[lr[i][1] - 1] = -1
    else:
        dp[lr[i][1] - 1] = cnt
        cnt += 1

sub = []
ans = []
st = -1
go = -1
for i in range(len(s)):
    if dp[i] in sub:
        sub.remove(dp[i])
        go = i
    elif dp[i] != -1:
        sub.append(dp[i])
        if st == -1:
            st = i
    if len(sub) == 0 and st != -1 and go != -1:
        d = s[st: go + 1]
        d.sort()
        ans += d
        st = -1
        go = -1
    if dp[i] == -1 and st == -1:
        ans.append(s[i])

ans = ''.join(ans)
print(ans)
n = int(input())
ans = []
for i in range(n):
    a = list(input())
    b = list(input())
    lena = len(a)
    lenb = len(b)

    dp = [[0] * (len(a) + 1) for j in range(lenb + 1)]
    for j in range(lenb):
        for k in range(lena):
            if b[j] == a[k]:
                dp[j + 1][k + 1] = dp[j][k] + 1
            else:
                dp[j + 1][k + 1] = max(dp[j][k], dp[j][k + 1])
    ans.append(dp[lenb][lena])

for i in ans:
    print(i)
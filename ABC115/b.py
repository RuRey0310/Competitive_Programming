n = int(input())
p = [int(input()) for i in range(n)]

maxprice = max(p)

ans = 0
for i in range(n):
    if maxprice == p[i]:
        ans += maxprice // 2
        maxprice = 0
    else:
        ans += p[i]

print(ans)

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

ans = 0
bai = 0
for i in range(k):
    if bai < x:
        ans += (a[i] * 2)
        bai += 1
    else:
        ans += a[i]

print(ans)
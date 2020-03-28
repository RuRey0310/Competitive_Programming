k, n = map(int, input().split())
a = list(map(int, input().split()))

ans = a[n - 1] - a[0]
for i in range(1,n):
    sub = (k - a[i]) + a[i - 1]
    ans = min(ans,sub)

print(ans)
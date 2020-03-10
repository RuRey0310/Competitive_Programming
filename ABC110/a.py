a = list(map(int, input().split()))

ans = max(a) * 10
del a[a.index(max(a))]
ans += max(a)
print(ans + min(a))

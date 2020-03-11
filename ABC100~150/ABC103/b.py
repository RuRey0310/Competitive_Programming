a = list(map(int, input().split()))

a.sort()

ans = 0
for i in range(1,3):
    ans += abs(a[i] - a[i - 1])

print(ans)

n = int(input())
a = list(map(int, input().split()))

sub = sum(a)
s = 0
ans = (10 ** 10) + 100
for i in range(n):
    s += a[i]
    if (i + 1) < n:
        ans = min(ans, abs(sub - (2 * s)))

print(ans)
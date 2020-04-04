n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)
sub = sum(a)
ans = 0
touhyou = sub * (1 / (4 * m))
for i in range(n):
    if a[i] >= touhyou:
        ans += 1

if ans >= m:
    print("Yes")
else:
    print("No")
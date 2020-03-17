n, m = map(int, input().split())
a, b = map(int, input().split())

ans1 = b
for i in range(n - m + 1):
    ans1 += a

ans2 = 0
for i in range(m):
    ans2 += a

print(min(ans1, ans2))
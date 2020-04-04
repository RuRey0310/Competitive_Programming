n, m, x = map(int, input().split())
a = list(map(int, input().split()))

ans1 = 0
for i in range(0, x + 1):
    if i in a:
        ans1 += 1

ans2 = 0
for i in range(x, n + 1):
    if i in a:
        ans2 += 1

print(min(ans1, ans2))
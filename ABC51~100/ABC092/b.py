n = int(input())
d, x = map(int, input().split())
a = [int(input()) for i in range(n)]

ans = x
for i in a:
    ans += 1
    for j in range(1, d + 1):
        sub = (i * j) + 1
        if sub > d:
            break
        ans += 1

print(ans)
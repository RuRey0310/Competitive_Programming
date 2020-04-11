n = int(input())
d = [int(input()) for i in range(n)]

ans = 0
sub = 101
d.sort(reverse=True)
for i in range(n):
    if sub > d[i]:
        ans += 1
        sub = d[i]

print(ans)
import bisect
n = int(input())
a = list(map(int, input().split()))

tech = []
ful = []
a.sort(reverse=True)
for i in range(n * 2):
    if i % 2 == 0:
        tech.append(a[i])
    else:
        ful.append(a[i])

tech.sort(reverse=True)
ful.sort(reverse=True)
ans = 0
techcnt = 0
fulcnt = 0
while techcnt < n and fulcnt < n:
    if tech[techcnt] < ful[fulcnt]:
        ans += 1
        fulcnt += 1
        techcnt += 1
    else:
        techcnt += 1

print(ans)
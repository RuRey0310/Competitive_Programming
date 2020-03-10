n, x = map(int, input().split())
l = list(map(int, input().split()))


cnt = 1
d = 0
for i in range(n):
    if (x >= d + l[i]):
        cnt += 1
    d = d + l[i]

print(cnt)

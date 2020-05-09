n = int(input())

ans = 0
s = 0
for i in range(1, n + 1):
    sub = 0
    g = i
    while g >= 2:
        sub += 1
        g = g // 2
    if s < sub:
        ans = i
        s = sub

print(max(ans,1))
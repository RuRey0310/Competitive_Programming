l = int(input())

ans = 0
i = 0
while i < l:
    if (l - i) % 2 == 0:
        a = (l - i) / 2
        b = (l - i) / 2
    else:
        a = ((l - i) / 2)
        b = (l - i) / 2
    ans = max(ans, a * b * i)
    i += 0.001

print(ans)
n, a, b = map(int, input().split())

ans = 0
for i in range(1, n + 1):
    ii = str(i)
    ii = list(ii)
    sub = 0
    for j in ii:
        sub += int(j)
    if sub >= a and sub <= b:
        ans += i

print(ans)
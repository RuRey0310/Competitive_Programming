a, b = map(int, input().split())

ans = 0
for i in range(a, b + 1):
    s = str(i)
    s = list(s)
    for j in range(len(s) // 2):
        if s[j] != s[len(s) - 1 - j]:
            break
        if j == (len(s) // 2) - 1:
            ans += 1

print(ans)    
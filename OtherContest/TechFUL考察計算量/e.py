l = int(input())
s = list(input())
t = list(input())

ans = 0
for i in range(l):
    sub = abs(ord(s[i]) - ord(t[i]))
    ans += min(sub,26-sub)

print(ans)
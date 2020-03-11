s = list(map(int,input()))

ans = 0
for i in range(len(s) - 1):
    if s[i] == s[i+1]:
        ans += 1
        if s[i+1] == 0:
            s[i+1] = 1
        else:
            s[i+1] = 0
print(ans)

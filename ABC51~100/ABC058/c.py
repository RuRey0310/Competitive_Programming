n = int(input())
s = [list(input()) for i in range(n)]

save = {}
sub = {}
s[0].sort()
for i in range(len(s[0])):
    if s[0][i] in sub:
            save[s[0][1]] += 1
            sub[s[0][i]] += 1
    else:
        sub[s[0][i]] = 1
        save[s[0][1]] = 1

for i in range(1, n):
    s[i].sort()
    for j in range(len(s[i])):
        if s[i][j] in sub:
            sub[s[i][j]] -= 1
    for k in sub:
        if sub[k] <= 0:
            sub[k] = save[k]
        else:
            del sub[k]
    print(sub)
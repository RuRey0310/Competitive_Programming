n,m = map(int, input().split())
p,s = [0] * m, [0] * m
for i in range(m):
    p[i], s[i] = map(str, input().split())
    p[i] = int(p[i])

ac = 0
wa = 0
que = [False] * (n + 1)
wan = [0] * (n + 1)

for i in range(m):
    if que[p[i]] == False:
        if s[i] == "WA":
            wan[p[i]] += 1
        else:
            que[p[i]] = True

for i in range(len(que)):
    if que[i] == True:
        ac += 1
        wa += wan[i]

print(ac,wa)    

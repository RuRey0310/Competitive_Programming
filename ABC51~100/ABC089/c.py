n = int(input())
s = [list(input()) for i in range(n)]

p = [0, 0, 0, 0, 0, 0, 1, 1, 1, 2]
q = [1, 1, 1, 2, 2, 3, 2, 2, 3, 3]
r = [2, 3, 4, 3, 4, 4, 3, 4, 4, 4]

d = [0] * 5

for i in range(n):
    if s[i][0] == "M":
        d[0] += 1
    elif s[i][0] == "A":
        d[1] += 1
    elif s[i][0] == "R":
        d[2] += 1
    elif s[i][0] == "C":
        d[3] += 1
    elif s[i][0] == "H":
        d[4] += 1
        
ans = 0
for i in range(0,10):
    ans += (d[p[i]] * d[q[i]] * d[r[i]])
print(ans)
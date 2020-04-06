import collections
n = int(input())
s = [input() for i in range(n)]
m = int(input())
t = [input() for i in range(m)]

ss = collections.Counter(s)
tt = collections.Counter(t)
ans = 0
for i in ss:
    sub = ss[i]
    if i in tt:
        sub -= tt[i]
    ans = max(ans, sub)
    
print(ans)
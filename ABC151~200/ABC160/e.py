x, y, a, b, c = map(int, input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)

a = []
for i in range(x):
    a.append(p[i])

for i in range(y):
    a.append(q[i])

for i in range(c):
    a.append(r[i])

a.sort(reverse=True)
ans = 0
for i in range(x + y):
    ans += a[i]

print(ans)
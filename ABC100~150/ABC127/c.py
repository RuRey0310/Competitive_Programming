n,m = map(int,input().split())
l,r = [0] * m, [0] * m
for i in range(m):
    l[i], r[i] = map(int, input().split())

lmax = 0
rmin = 10 ** 5
for i in range(m):
    lmax = max(lmax,l[i])
    rmin = min(rmin,r[i])

if lmax <= rmin:
    print(rmin - lmax + 1)
else:
    print("0")

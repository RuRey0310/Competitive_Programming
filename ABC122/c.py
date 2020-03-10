n, q = map(int, input().split())
s = list(input())
l,r = [0] * q, [0] * q
for i in range(q):
    l[i], r[i] = map(int, input().split())

#acの場所把握
ac = [0] * (n + 1)
for i in range(n - 1):
    if s[i] == "A" and s[i + 1] == "C":
        ac[i + 1] = ac[i] + 1
    else:
        ac[i + 1] = ac[i]

for i in range(q):
    print(ac[r[i] - 1] - ac[l[i] - 1])


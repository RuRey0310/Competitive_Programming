import itertools
n = int(input())
k = int(input())
c = []
for i in range(n):
    c.append(int(input()))

sub = []
ans = 0
for j in itertools.combinations(c, k):
    string = ""
    print(j)
    for l in range(k):
        string += str(j[l])
    mat = int(string)
    if mat in sub:
        continue
    ans += 1
    sub.append(mat)

print(ans)
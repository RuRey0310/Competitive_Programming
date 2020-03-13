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
    string2 = ""
    print(j)
    for l in range(k):
        string2 = str(j[l]) + string2
        string += str(j[l])
    met = int(string2)
    mat = int(string)
    print(met,mat)
    if not mat in sub:
        ans += 1
        sub.append(mat)
    if not met in sub:
        ans += 1
        sub.append(met)

print(ans)
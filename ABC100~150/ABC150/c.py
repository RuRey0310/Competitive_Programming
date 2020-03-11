import itertools
import math

n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

li = [0] * n
for i in range(n):
    li[i] = i + 1

sub = list(itertools.permutations(li, n))

pans = 0
qans = 0
so = math.factorial(n)
for i in range(so):
    for j in range(n):
        if sub[i][j] != p[j]:
            break
        if j == n - 1:
            pans = i + 1

for i in range(so):
    for j in range(n):
        if sub[i][j] != q[j]:
            break
        if j == n - 1:
            qans = i + 1

print(max(pans, qans) - min(pans, qans))

import itertools
from collections import defaultdict
import collections
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

n, m, x = map(int, input().split())
ca = [list(map(int, input().split())) for i in range(n)]

ans = mod
for i in range(2 ** n):
    alg = [0] * (m+1)
    switch = [0] * n
    for j in range(n):
        if((i >> j) & 1):
            switch[j] = 1
    for k in range(n):
        for l in range(m + 1):
            if switch[k] == 1:
                alg[l] += ca[k][l]
    for y in range(m+1):
        if y != 0:
            if x > alg[y]:
                break
        if y == m:
            ans = min(ans, alg[0])

if ans == mod:
    print("-1")
else:
    print(ans)
#デフォルト
import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(k):
    ans = [0] * n
    for j in range(n):
        for l in range(max(0,j - a[j]), min(n,j + a[j] + 1)):
            ans[l] += 1
    if ans.count(n) == n:
        break
    else:
        for g in range(n):
            a[g] = ans[g]

for i in range(n):
    print(ans[i],end=" ")
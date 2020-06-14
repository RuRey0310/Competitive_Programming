#デフォルト
import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

x, n = map(int, input().split())
p = list(map(int, input().split()))

sub = [False] * 210
for i in range(n):
    sub[p[i] + 105] = True
sub[x] = True

ans = mod
nn = 0
for i in range(210):
    if not sub[i]:
        if ans > abs((i - 105) - x):
            nn = i - 105
            ans = abs((i - 105) - x)
            

print(nn)
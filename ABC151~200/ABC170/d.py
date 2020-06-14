#デフォルト
import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

n = int(input())
a = list(map(int, input().split()))

a.sort()
tf = [False] * (10 ** 6 + 1)
ans = 0
if a[0] == 1:
    print("0")
else:
    for i in range(n):
        cnt = a[i]
        cc = 1
        if i != n -1:
            ll = i + 1
        else:
            ll = i - 1
        if not tf[cnt] and a[i] != a[ll]:
            ans += 1
            while cnt * cc <= max(a):
                tf[cnt * cc] = True
                cc += 1

    print(ans)

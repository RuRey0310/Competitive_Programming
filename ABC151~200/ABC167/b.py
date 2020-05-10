import itertools
from collections import defaultdict
import collections
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

a, b, c, k = map(int, input().split())

ans = 0
if a >= k:
    print(k)
elif a + b >= k:
    print(a)
else:
    print(a - (k - a-b))
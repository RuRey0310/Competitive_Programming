import itertools
from collections import defaultdict
import collections
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

s = list(input())
t = list(input())

ss = ''.join(s)
tt = ""
for i in range(len(t) - 1):
    tt += t[i]

if ss == tt:
    print("Yes")
else:
    print("No")
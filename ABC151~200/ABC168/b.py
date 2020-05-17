import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

k = int(input())
s = list(input())

if len(s) > k:
    for i in range(k):
        print(s[i], end="")
    print("...")
else:
    s = ''.join(s)
    print(s)
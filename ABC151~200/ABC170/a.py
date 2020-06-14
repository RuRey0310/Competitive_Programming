#デフォルト
import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

x = list(map(int,input().split()))

for i in range(5):
    if x[i] != i + 1:
        print(i+1)
        break

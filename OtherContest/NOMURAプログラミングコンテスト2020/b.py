#デフォルト
import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

t = list(input())

for i in range(len(t)):
    if (t[i] == "?"):
        print("D",end="")
    else:
        print(t[i],end="")
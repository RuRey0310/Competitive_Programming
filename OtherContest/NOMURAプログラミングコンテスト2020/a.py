#デフォルト
import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

h1, m1, h2, m2, k = map(int, input().split())

minute = ((h2 * 60) + m2) - ((h1 * 60) + m1)

print(minute - k)
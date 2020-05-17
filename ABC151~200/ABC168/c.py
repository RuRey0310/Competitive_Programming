import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

a, b, h, m = map(int, input().split())

subh = 30 * h
subh += 0.5 * m
subm = 6 * m

kakudo = min(abs(subh - subm), 360 - abs(subh - subm))
ans = a ** 2 + b ** 2 - ((2 * a * b) * (math.cos(math.radians(kakudo))))
print(math.sqrt(ans))
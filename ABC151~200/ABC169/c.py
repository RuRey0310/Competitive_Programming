#デフォルト
import itertools
from collections import defaultdict
import collections
import math
import sys
from decimal import *
sys.setrecursionlimit(200000)
mod = 1000000007

a, b = map(Decimal, input().split())

print(math.floor(a * b))
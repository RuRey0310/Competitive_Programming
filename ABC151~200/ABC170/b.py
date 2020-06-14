#デフォルト
import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

x, y = map(int, input().split())

flag = False
for i in range(x + 1):
    for j in range((x + 1) - i):
        if (i * 2 + j * 4) == y and i+j== x:
            flag = True

if flag == False:
    print("No")
else:
    print("Yes")
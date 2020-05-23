import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

s = list(input())
t = list(input())

same = 0
case = 0
for i in range(len(s)):
    if s[i] == t[i]:
        same += 1
    if s[i].upper() == t[i].upper():
        case += 1

if same == 3:
    print("same")
elif case == 3:
    print("case-insensitive")
else:
    print("different")
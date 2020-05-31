#デフォルト
import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

n = int(input())
a = list(map(int,input().split()))

ans = 1
sub = 10 ** 18
for i in range(n):
    if a[i] == 0:
        print("0")
        exit()
for i in a:
    ans *= i
    if ans > sub:
        ans = -1
        break

print(ans)
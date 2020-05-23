import itertools
from collections import defaultdict
import collections
import math
import sys
sys.setrecursionlimit(200000)
mod = 1000000007

n, m, q = map(int, input().split())
s = [list(map(int, input().split())) for i in range(q)]

player = [[] for i in range(n + 1)]
score = [0] * (m + 1)
for i in range(q):
    if s[i][0] == 1:
        sub = 0
        for i in player[s[i][1]]:
            sub += n-score[i]
        print(sub)
    else:
        score[s[i][2]] += 1
        player[s[i][1]].append(s[i][2])
import itertools
from collections import defaultdict
import collections
mod = 1000000007
n, k = map(int, input().split())

s = [i for i in range(n + 1)]
cumsum = itertools.accumulate(s)
cumsum = list(cumsum)

ans = 0
for i in range(k, n + 1):
    a = cumsum[i - 1] - cumsum[0]
    b = cumsum[n] - cumsum[n - i]
    ans += (b - a + 1) % mod

print((ans + 1) % mod)
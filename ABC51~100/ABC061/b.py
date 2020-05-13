n, m = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(m)]

from collections import defaultdict
d = defaultdict(int)
for i in range(m):
    d[ab[i][0]] += 1
    d[ab[i][1]] += 1

for i in range(1, n + 1):
    print(d[i])
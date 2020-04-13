import collections
n = int(input())
a = [int(input()) for i in range(n)]

ans = 0
aa = collections.Counter(a)

for i in aa:
    if aa[i] >= 2:
        ans += aa[i] - 1

print(ans)
import collections
n, k = map(int, input().split())
a = list(map(int, input().split()))

aa = collections.Counter(a)
sub = []
for i in aa:
    sub.append(aa[i])

sub.sort()
ans = 0
for i in range(len(sub) - k):
    ans += sub[i]

print(ans)
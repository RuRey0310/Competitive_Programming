import collections
n = int(input())
a = list(map(int,input().split()))

sub = collections.Counter(a)
ans = 0
for i in sub:
    ans += sub[i] * (sub[i] - 1) // 2
for i in range(n):
    ad = sub[a[i]] * (sub[a[i]] - 1) // 2 - ((sub[a[i]] - 1) * (sub[a[i]] - 2) // 2)
    print(ans - ad)
import collections
n = int(input())
a = list(map(int, input().split()))

aa = collections.Counter(a)
ans = 0
for i in aa:
    if i != aa[i]:
        if aa[i] < i:
            ans += aa[i]
        else:
            ans += aa[i] - i
print(ans)
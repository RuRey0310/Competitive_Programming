import collections
n = int(input())
a = [int(input()) for i in range(n)]

aa = collections.Counter(a)
ans = 0
for i in aa:
    if aa[i] % 2 == 1:
        ans += 1
    
print(ans)
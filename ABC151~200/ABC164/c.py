import collections
n = int(input())
s = [input() for i in range(n)]

ans = collections.Counter(s)
print(len(ans))
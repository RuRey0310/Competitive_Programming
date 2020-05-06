from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

left = defaultdict(int)
for i in range(n):
    left[i + a[i]] += 1

ans = 0
for i in range(n):
    sub = i - a[i]
    if sub in left:
        ans += left[sub]

print(ans)
import bisect
n = int(input())
x = list(map(int, input().split()))

cp = sorted(x, reverse=False)
for i in range(n):
    s = bisect.bisect_left(cp, x[i])
    if s + 1 <= n // 2:
        print(cp[n // 2])
    else:
        print(cp[(n // 2) - 1])

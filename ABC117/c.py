n, m = map(int, input().split())
x = list(map(int, input().split()))

xsort = sorted(x)

if n >= m:
    print("0")
else:
    ans = xsort[m - 1] - xsort[0]
    masum = [0] * m
    for i in range(m - 1):
        masum[i] = xsort[i + 1] - xsort[i]
    sum = sorted(masum)
    for i in range(n - 1):
        ans -= sum[len(sum) - 1 - i]
    print(ans)

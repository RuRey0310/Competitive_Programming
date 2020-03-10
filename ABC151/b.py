n,k,m = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
for i in range(n - 1):
    sum += a[i]

ans = 0
for i in range(k + 1):
    if (sum + i) / n >= m:
        ans = i
        break
    else:
        ans = -1
print(ans)

n, l = map(int, input().split())


sum = 0
for i in range(n):
    sum += i + l

min = 10000
ans = 0
for i in range(n):
    msum = 0
    for j in range(n):
        if (i != j):
            msum += j + l
    if (abs(sum - msum) < min):
        min = abs(sum-msum)
        ans = msum

print(ans)

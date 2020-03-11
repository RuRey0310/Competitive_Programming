n,k = map(int,input().split())

ans = 0
for i in range(1,n + 1):
    double = i
    for j in range(1000):
        if double >= k:
            break
        else:
            double = double << 1
    ans += (1 / n) * ((1 / 2)**j)

print(ans)

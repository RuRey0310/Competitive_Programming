n, m = map(int, input().split())
h = list(map(int, input().split()))
k = [list(map(int, list(input().split()))) for i in range(m)]

d = [0] * n
for i in range(m):
    d[k[i][0] - 1] = max(d[k[i][0] - 1], h[k[i][1] - 1])
    d[k[i][1] - 1] = max(d[k[i][1] - 1], h[k[i][0] - 1])
    
ans = 0
for i in range(n):
    if h[i] > d[i]:
        ans += 1

print(ans)
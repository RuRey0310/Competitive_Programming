n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = float("inf")
k -= 1
for i in range(k, n):
    sub = abs(x[i] - x[i - k]) + min(abs(x[i]), abs(x[i - k]))
    ans = min(ans, sub)
    
print(ans)

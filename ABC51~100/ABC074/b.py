n = int(input())
k = int(input())
x = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += min(x[i] * 2, abs(k - x[i]) * 2)

print(ans)
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(m):
        ans += a[i] ^ b[j]

print(ans)
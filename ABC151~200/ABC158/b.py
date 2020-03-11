n, a, b = map(int, input().split())

ans = a * (n // (a + b))
if a < n % (a + b):
    ans += a
else:
    ans += n % (a + b)

print(ans)

n, a, b = map(int, input().split())
mod = (10 ** 9) + 7

ans = pow(2, n, mod) - 1
an = 1
for i in range(n - a + 1, n + 1):
    an *= i
    an %= mod
for i in range(1, a + 1):
    an *= pow(i, mod - 2, mod)
    an %= mod
bn = 1
for i in range(n - b + 1, n + 1):
    bn *= i
    bn %= mod
for i in range(1, b + 1):
    bn *= pow(i, mod - 2, mod)
    bn %= mod

ans -= (an + bn)
print(ans % mod)

import math
n, m = map(int, input().split())

mod = (10 ** 9) + 7
if abs(n - m) >= 2:
    print("0")
else:
    nn = math.factorial(n)
    mm = math.factorial(m)
    if abs(n - m) >= 1:
        print((nn * mm) % mod)
    else:
        ans = nn * 2 % mod
        ans = ans * mm % mod
        print(ans)
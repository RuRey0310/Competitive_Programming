import math


def lcm(a, b):
    return a * b // gcd(a, b)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a, b, c, d = map(int, input().split())
ans = 0

# 最小公倍数
cd = lcm(c, d)

bdiv = (b // c) + (b // d) - (b // cd)
adiv = ((a - 1) // c) + ((a - 1) // d) - ((a - 1) // cd)
ans = (b - a) - (bdiv - adiv) + 1

print(ans)

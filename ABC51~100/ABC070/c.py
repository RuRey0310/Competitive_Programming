n = int(input())
t = [int(input()) for i in range(n)]

#最大公約数
def gcd(a, b):
    while b!=0:
        a,b=b,a%b
    return a

#最小公倍数
def lcm(a,b):
    return a * b // gcd(a, b)

ans = t[0]
for i in range(1,n):
    ans = lcm(ans, t[i])

print(ans)
n = int(input())
a = list(map(int, input().split()))
div = (10 ** 9) + 7

#最大公約数
def gcb(a, b):
    while b!=0:
        a,b=b,a%b
    return a

#最小公倍数
def lcm(a,b):
    return a * b // gcb(a, b)

lc = 1
for i in range(n):
    lc = lcm(lc, a[i])

ans = 0
for i in range(n):
    ans += lc // a[i]
print(ans % div)

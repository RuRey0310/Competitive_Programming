n, X = map(int, input().split())
x = list(map(int, input().split()))

#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)

x.append(X)

dis = x[1] - x[0]
for i in range(n):
    dis = gcd(x[i + 1] - x[i], dis)

print(abs(dis))

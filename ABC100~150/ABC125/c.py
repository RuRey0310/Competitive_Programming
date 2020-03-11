n = int(input())
a = list(map(int,input().split()))

def gcd(a, b):
    while b!=0:
        a,b=b,a%b
    return a

l = [0] * (n + 1)
r = [0] * (n + 1)
for i in range(n):
    l[i + 1] = gcd(l[i], a[i])

for i in reversed(range(n)):
    r[i] = gcd(r[i + 1], a[i])

ans = 0
for i in range(n):
    ans = max(ans, gcd(l[i], r[i + 1]))

print(ans)

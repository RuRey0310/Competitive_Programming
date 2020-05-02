import math
x = int(input())

a = 100
ans = 0
while x > a:
    a = math.floor(a*1.01)
    ans += 1

print(ans)
x = int(input())

ans = 0
while 4096 > x:
    x *= 2
    ans += 1

print(ans)
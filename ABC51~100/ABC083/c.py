x,y = map(int,input().split())

ans = 0
sy = x
while sy <= y:
    sy *= 2
    ans += 1

print(ans)
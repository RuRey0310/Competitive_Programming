n, m = map(int, input().split())
k=[list(map(int,list(input().split()))) for i in range(n)]


ans = 0
k.sort()
for i in range(n):
    ml = min(k[i][1],m)
    ans += k[i][0] * ml
    m -= k[i][1]
    if m <= 0:
        break
print(ans)

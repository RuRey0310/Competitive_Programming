n, x = map(int, input().split())
m = [int(input()) for i in range(n)]

m.sort()

ans = 0
for i in range(n):
    if x >= m[i]:
        ans += 1
        x -= m[i]

while x >= m[0]:
    ans += 1
    x -= m[0]
    
print(ans)
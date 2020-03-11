a,b,t = map(int,input().split())

ans = 0
t += 0.5
i = 1
while(i < t):
    if(i % a == 0):
        ans += b
    i += 1

print(ans)

n,m = map(int,input().split())
s=[list(map(int,list(input().split()))) for i in range(m)]
p = list(map(int,input().split()))

ans = 0
for i in range(2 ** n):
    #1の時は点灯
    switch = [0] * n
    for j in range(n):
        if((i >> j) & 1):
            switch[j] = 1
    for k in range(m):
        cnt = 0
        for l in range(1,s[k][0] + 1):
            if(switch[s[k][l] - 1] == 1):
                cnt += 1
        if(cnt % 2 != p[k]):
            break
        if(k == m - 1):
            ans += 1    

print(ans)

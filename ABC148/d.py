n = int(input())
a = list(map(int,input().split()))

broke = 0
cnt = 1
for i in range(n):
    if a[i] != cnt:
        broke += 1
    else:
        cnt += 1

if broke == n:
    print("-1")
else:
    print(broke)

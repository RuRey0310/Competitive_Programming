n = int(input())
a = list(map(int, input().split()))

ans = 0
cnt = 0
for i in range(n):
    if a[i] % 4 == 0:
        ans += 1
    elif a[i] % 2 == 0:
        cnt += 1
        if cnt % 2 == 0:
            ans += 1
    

if n // 2 <= ans:
    print("Yes")
else:
    print("No")
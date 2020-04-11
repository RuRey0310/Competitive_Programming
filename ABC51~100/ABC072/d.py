n = int(input())
p = list(map(int, input().split()))

ans = 0
flag = 0
for i in range(1, n + 1):
    if p[i - 1] == i:
        if flag != 0:
            if i - 1 == flag:
                ans += 0
                flag = 0
            else:
                ans += 1
                flag = i
            continue
        flag = i
        ans += 1

print(ans)

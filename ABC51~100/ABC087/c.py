n = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

ans = 0
for i in range(n):
    sub = 0
    for j in range(n):
        if i == j:
            sub += a1[j]
            sub += a2[j]
        elif i < j:
            sub += a2[j]
        else:
            sub += a1[j]
    ans = max(sub, ans)

print(ans)
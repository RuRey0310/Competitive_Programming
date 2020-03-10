k = int(input())

ans = 0
for i in range(2, k + 1):
    if i % 2 == 0:
        for j in range(1, k + 1):
            if j % 2 == 1:
                ans += 1

print(ans)

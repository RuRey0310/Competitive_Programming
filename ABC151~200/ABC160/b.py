n = int(input())

coin = [500, 5, 100, 50, 10, 1]

ans = 0
for i in range(6):
    if i == 0:
        ans += (n // coin[i]) * 1000
    if i == 1:
        ans += (n // coin[i]) * 5
    n = n % coin[i]

print(ans)
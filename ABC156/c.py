n = int(input())
x = list(map(int, input().split()))

ans = float("inf")

for i in range(101):
    sub = 0
    for j in range(n):
        sub += (x[j] - i) ** 2
    ans = min(ans, sub)

print(ans)

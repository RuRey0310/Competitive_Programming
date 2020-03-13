m = int(input())

n = 1000 - m
money = [500, 100, 50, 10, 5, 1]
ans = 0
for i in range(6):
    ans += n // money[i]
    n = n % money[i]

print(ans)
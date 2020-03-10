n,m = map(int, input().split())
a=[list(map(int,list(input().split()))) for i in range(n)]

food = [0] * (m + 1)

for i in range(n):
    for j in range(1, a[i][0] + 1):
        food[a[i][j]] += 1

print(food.count(n))

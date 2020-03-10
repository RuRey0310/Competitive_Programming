import math
food = [int(input()) for i in range(5)]

minute = 9
z = 0
for i in range(4):
    if minute > food[i] % 10 and food[i] % 10 != 0:
        minute = food[i] % 10
        z = i

ans = 0
for i in range(5):
    if z != i:
        ans += math.ceil(food[i] / 10) * 10
ans += food[z]

print(ans)

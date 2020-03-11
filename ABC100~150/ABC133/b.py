import math

n, d = map(int, input().split())

con = [list(map(int, input().split())) for i in range(n)]

cnt = 0
sum = 0

for i in range(n-1):

    for j in range(i + 1, n):

        for k in range(d):
            sum += (con[i][k] - con[j][k]) ** 2

        if ((sum**0.5).is_integer()):
            cnt += 1
        sum = 0

print(cnt)

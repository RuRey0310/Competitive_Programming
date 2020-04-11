n, y = map(int, input().split())

y = y // 1000

yen = 0
for i in range(n + 1):
    for j in range(n + 1 - i):
        yen = (i * 10) + (j * 5)
        if i + j + (y - yen) == n and yen <= y:
            print(i, j, y - yen)
            exit()

print("-1 -1 -1")

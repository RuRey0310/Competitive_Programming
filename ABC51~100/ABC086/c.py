n = int(input())
txy = [list(map(int, input().split())) for i in range(n)]

x = 0
y = 0
t = 0
for i in range(n):
    sub = abs(txy[i][1] - x) + abs(txy[i][2] - y)
    if txy[i][0] - t < sub:
        print("No")
        exit()
    if txy[i][0] - t != sub:
        if (txy[i][0] - t) % 2 == 0:
            if sub % 2 != 0:
                print("No")
                exit()
        else:
            if sub % 2 != 1:
                print("No")
                exit()

    t = txy[i][0]
    x = txy[i][1]
    y = txy[i][2]

print("Yes")
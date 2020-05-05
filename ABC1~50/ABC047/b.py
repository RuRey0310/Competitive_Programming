w, h, n = map(int, input().split())
xya = [list(map(int, input().split())) for i in range(n)]

box = [[True for i in range(w)]for j in range(h)]
for i in range(n):
    if xya[i][2] == 1:
        for j in range(xya[i][0]):
            for k in range(h):
                box[k][j] = False
    elif xya[i][2] == 2:
        for j in range(xya[i][0], w):
            for k in range(h):
                box[k][j] = False
    elif xya[i][2] == 3:
        for j in range(w):
            for k in range(xya[i][1]):
                box[k][j] = False
    else:
        for j in range(w):
            for k in range(xya[i][1], h):
                box[k][j] = False

ans = 0
for i in range(h):
    for j in range(w):
        if box[i][j]:
            ans += 1

print(ans)
h, w = map(int, input().split())
k = [list(input()) for i in range(h)]

dx = [1, 0]
dy = [0, 1]
boo = [[False] * (w) for i in range(h)]
def dfs(x, y):
    boo[x][y] = True
    if x == h and y == w:
        return
    for i in range(2):
        nextx = dx[i] + x
        nexty = dy[i] + y
        if nextx < h and nexty < w and k[nextx][nexty] != "#" and boo[nextx][nexty] == False:
            dfs(nextx, nexty)
    return

if k[0][0] != "#":
    dfs(0, 0)

if boo[h - 1][w - 1]:
    print("0")
else:
    for i in range(h):
        for j in range(w):
            if k[i][j] == "#":
                
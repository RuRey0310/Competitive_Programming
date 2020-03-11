import queue
h, w = map(int, input().split())
a = [list(input()) for i in range(h)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
aa = [["W"] * w for i in range(h)]
def bfs(sx, sy):
    q = queue.Queue()
    q.put([sx, sy])
    aa[sx][sy] = "B"
    while not q.empty():
        now = q.get()
        nowx = now[0]
        nowy = now[1]
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            if nextx >= 0 and nexty >= 0 and nextx < h and nexty < w:
                if aa[nextx][nexty] == "W" and a[nextx][nexty] != "#":
                    aa[nextx][nexty] = "B"

for i in range(h):
    for j in range(w):
        if a[i][j] == ".":
            flag = True
            break
        else:
            flag = False

ans = 0
while flag:
    for i in range(h):
        for j in range(w):
            if a[i][j] == "#":
                bfs(i, j)
    ans += 1
    flag = False
    for i in range(h):
        for j in range(w):
            if aa[i][j] == "B":
                a[i][j] = "#"
            else:
                flag = True

print(ans)
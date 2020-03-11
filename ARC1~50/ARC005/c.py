import queue
h,w = map(int,input().split())
c = [list(input()) for i in range(h)]

cc = [[[False] * w for i in range(h)] for j in range(3)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(sx, sy):
    q = queue.Queue()
    q.put([sx, sy, 0])
    cc[0][sx][sy] = True
    while not q.empty():
        now = q.get()
        nowx = now[0]
        nowy = now[1]
        nowb = now[2]
        for i in range(4):
            nextx = nowx + dx[i]
            nexty = nowy + dy[i]
            if nextx >= 0 and nexty >= 0 and nextx < h and nexty < w:
                if cc[nowb][nextx][nexty] == False:
                    if nowb < 2 and c[nextx][nexty] == "#":
                        q.put([nextx, nexty, nowb + 1])
                        cc[nowb + 1][nextx][nexty] = True
                    elif c[nextx][nexty] != "#":
                        q.put([nextx, nexty, nowb])
                        cc[nowb][nextx][nexty] = True

for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            bfs(i, j)
        if c[i][j] == "g":
            gx = i
            gy = j

for i in range(3):
    if cc[i][gx][gy]:
        print("YES")
        exit()
print("NO")
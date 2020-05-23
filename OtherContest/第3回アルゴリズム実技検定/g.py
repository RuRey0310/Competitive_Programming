import queue
n, x, y = map(int, input().split())
xy = [["."] * 409 for i in range(409)]
for i in range(n):
    xx, yy = map(int, input().split())
    xy[205 + xx][205 + yy] = "#"

def bfs(vx, vy):
    nx = [1, 0, -1, 1, -1, 0]   
    ny = [1, 1, 1, 0, 0, -1]
    q = queue.Queue()
    q.put([vx, vy])
    tf[vx][vy] = True
    cnt[vx][vy] = 0
    while not q.empty():
        sub = q.get()
        nowx = sub[0]
        nowy = sub[1]
        for i in range(6):
            nextx = nowx + nx[i]
            nexty = nowy + ny[i]
            if nextx > 408 or nexty > 408 or nextx < 0 or nexty < 0:
                continue
            if xy[nextx][nexty] == "#":
                continue
            if tf[nextx][nexty]:
                continue
            tf[nextx][nexty] = True
            cnt[nextx][nexty] = cnt[nowx][nowy] + 1
            q.put([nextx, nexty])

tf = [[False] * 409 for i in range(409)]
cnt = [[0] * 409 for i in range(409)]
bfs(205, 205)
if tf[205 + x][205 + y] == False:
    print("-1")
else:
    print(cnt[205 + x][205 + y])

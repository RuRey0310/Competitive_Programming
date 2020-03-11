import queue
h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
INF = float("inf")
ss = [[INF] * w for i in range(h)]
def bfs():
    q = queue.Queue()
    ss[0][0] = 1
    q.put([0, 0])
    while not q.empty():
        now = q.get()
        nowx = now[0]
        nowy = now[1]
        for i in range(4):
            nextx = dx[i] + nowx
            nexty = dy[i] + nowy
            if nextx >= 0 and nexty >= 0 and nextx < h and nexty < w:
                if s[nextx][nexty] == "." and ss[nextx][nexty] == INF:
                    ss[nextx][nexty] = ss[nowx][nowy] + 1
                    q.put([nextx, nexty])

bfs()
cnt = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            cnt += 1

if ss[h - 1][w - 1] == INF:
    print("-1")
else:  
    print(cnt - ss[h - 1][w - 1])
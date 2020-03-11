import queue

H, W = map(int, input().split())
S = [input() for i in range(H)]
q = queue.Queue()
longest_path = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            g = [[0 if S[k][l] == '.' else -1 for l in range(W)] for k in range(H)]
            q.put((i,j))
            g[i][j] = 0
            while not(q.empty()):
                x, y = q.get()
                for nx, ny in [(x+1, y),(x-1, y),(x, y+1),(x, y-1)]:
                    if nx < 0 or nx > H-1 or ny < 0 or ny > W-1: continue
                    if g[nx][ny] != 0: continue
                    if nx == i and ny == j: continue
                    g[nx][ny] = g[x][y] + 1
                    q.put((nx,ny))
            longest_path = max(longest_path, max(map(max, g)))
print(longest_path)

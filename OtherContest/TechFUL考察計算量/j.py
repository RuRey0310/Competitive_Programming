import queue
n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[u].append([v, c])
    graph[v].append([u, c])

q = int(input())
xyt = [list(map(int, input().split())) for i in range(q)]

mod = 1000000007
def bbfs(x, maxdepth, goal):
    tf = [False] * (n + 1)    
    q = queue.Queue()
    tf[1] = True
    q.put([x, 1, 1])
    while not q.empty():
        sub = q.get()
        now = sub[0]
        depth = sub[1]
        cost = sub[2]
        if depth > maxdepth:
            continue
        for next in graph[now]:
            if tf[next[0]]:
                continue
            tf[next[0]] = True
            q.put([next[0], depth + 1, cost * next[1] % mod])
    return tf[goal]

def bfs(x, maxdepth, goal):
    bfans = 0
    q = queue.Queue()
    q.put([x, 1, 1])
    while not q.empty():
        sub = q.get()
        now = sub[0]
        depth = sub[1]
        cost = sub[2]
        if depth > maxdepth:
            if now == goal:
                bfans += cost
                bfans %= mod
            continue
        for next in graph[now]:
            q.put([next[0], depth + 1, cost * next[1] % mod])
    return bfans

for i in range(q):
    ans = bbfs(xyt[i][0],xyt[i][2],xyt[i][1])
    if not ans:
        print("0")
    else:
        ans = bfs(xyt[i][0],xyt[i][2],xyt[i][1]) % mod
        print(ans)

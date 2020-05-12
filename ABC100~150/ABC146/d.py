n = int(input())
a = []
b = []
# graph作成
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    a.append(u)
    b.append(v)

def dfs(x, depth,col):
    tf[x] = True
    if depth % 2 == 1:
        col = 0
    for next in graph[x]:
        if tf[next]:
            continue
        col += 1
        dfs(next, depth + 1, col)
        color[x, next] = col
        color[next, x] = col
    return

maxcolor = 0
tf = [False] * (n + 1)
color = {}
dfs(1, 1, 0)

print(max(color.values()))
for i in range(n - 1):
    print(color[a[i],b[i]])

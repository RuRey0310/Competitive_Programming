import sys
sys.setrecursionlimit(200000)
n = int(input())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    u, v, ww = map(int, input().split())
    graph[u].append([v,ww])
    graph[v].append([u,ww])
color = [-1] * n

def dfs(x):
    for sub in graph[x]:
        next = sub[0]
        lon = sub[1]
        if color[next - 1] != -1:
            continue
        if lon % 2 == 0:
            color[next - 1] = color[x - 1]
        else:
            if color[x - 1] == 1:
                color[next - 1] = 0
            else:
                color[next - 1] = 1
        dfs(next)

color[0] = 0
dfs(1)
for i in color:
    print(i)
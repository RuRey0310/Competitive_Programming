import sys
sys.setrecursionlimit(10 ** 5)

n, x, y = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
graph[x].append(y)
graph[y].append(x)
for i in range(1, n):
    graph[i].append(i + 1)
    graph[i + 1].append(i)

tf = [[False] * (n + 1) for i in range(n + 1)]
ans = [0] * (n + 1)
def dfs(now, before, depth):
    voi[now] = True
    next_graph = graph[now]
    if tf[now][before] == False and depth != 0:
        ans[depth] += 1
        tf[now][before] = True
        tf[before][now] = True
    for next in next_graph:
        if voi[next]:
            continue
        if next == before:
            continue
        dfs(next, now, depth + 1)
    return

for i in range(1, n + 1):
    voi = [False] * (n + 1)
    dfs(i, 0, 0)

print(ans)
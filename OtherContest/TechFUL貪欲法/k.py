import sys
sys.setrecursionlimit(10 ** 9)
n = int(input())
graph = {i: [] for i in range(1, n + 1)}
cost = [[0] * (n + 1) for i in range(n + 1)]
for _ in range(n - 1):
    u, d, w = map(int, input().split())
    graph[u].append(d)
    graph[d].append(u)
    cost[u][d] = w
    cost[d][u] = w     

q = int(input())
x, y = [0] * q, [0] * q
for i in range(q):
    x[i], y[i] = map(int, input().split())

INF = float("inf")
def dfs(v):
    seen[v] = True
    if seen[end]:
        return

    for next_v in graph[v]:
        if seen[next_v]: continue
        leng.append(str(cost[v][next_v]))
        dfs(next_v)
        if seen[end]:
            break
    
    if seen[end]:
        return
    else:
        del leng[-1]
        return

mod = (10 ** 9) + 7
for i in range(q):
    seen = [False] * (n + 1)
    end = y[i]
    leng = []
    dfs(x[i])
    leng.sort(reverse=True)
    leng = ''.join(leng)
    leng = int(leng)
    print(leng % mod)

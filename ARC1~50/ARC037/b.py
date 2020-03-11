n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(current, previous):
    tree = True
    for i in range(len(graph[current])):
        if graph[current][i] == previous:
            continue
        if visit[graph[current][i]]:
            tree = False
            return tree
        else:
            visit[graph[current][i]] = True
            if dfs(graph[current][i], current) == False:
                tree = False
    return tree
        

visit = [False] * (n + 1)
ans = 0
for i in range(1, n + 1):
    if visit[i]:
        continue
    visit[i] = True
    if dfs(i, 0):
        ans += 1

print(ans)

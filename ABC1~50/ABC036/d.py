n = int(input())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

mod = 10 ** 9 + 7
dpf = [0] * (n + 1)
dpg = [0] * (n + 1)
def f(x, root):
    if dpf[x] > 0:
        return dpf[x]
    
    white = g(x, root)
    black = 1
    for child in graph[x]:
        if child == root:
            continue
        black *= g(child, x)
    dpf[x] = white + black
    return dpf[x]
    
def g(x, root):
    if dpg[x] > 0:
        return dpg[x]
    
    count = 1
    for child in graph[x]:
        if child == root:
            continue

        count *= f(child, x)
    dpg[x] = count
    return dpg[x]
ans = f(1, -1)
print(ans % mod)
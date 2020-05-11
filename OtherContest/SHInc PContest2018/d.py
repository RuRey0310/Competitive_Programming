import heapq
INF = 10**18
def dijkstra(s, edge, n):
    d = [INF] * n
    used = [True] * n #True: not used
    d[s] = 0
    used[s] = False
    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist,e)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if not used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,(e[0]+d[v],e[1]))
    return d
 
n, m, s, t = map(int, input().split())
s -= 1
t -= 1
graph_a = [[] for _ in range(n)]
graph_b = [[] for _ in range(n)]
for i in range(m):
    u, v, a, b = map(int, input().split())
    u, v = u-1, v-1
    graph_a[u].append((a, v))
    graph_a[v].append((a, u))
    graph_b[u].append((b, v))
    graph_b[v].append((b, u))
 
yen = dijkstra(s, graph_a, n)
snu = dijkstra(t, graph_b, n)

cost = [0] * n
for i in range(n):
    cost[i] = (yen[i] + snu[i],i)

heapq.heapify(cost)
c = -1
aaa = 10 ** 15
for i in range(n):
    if c < i:
        while cost:
            nn, t = heapq.heappop(cost)
            if t >= i:
                c = t
                break
    print(aaa - nn)

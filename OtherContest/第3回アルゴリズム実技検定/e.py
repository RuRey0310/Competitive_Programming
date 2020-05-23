n, m, q = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
color = list(map(int, input().split()))
color.insert(0, 0)
s = [list(map(int,input().split())) for i in range(q)]

def change(x):
    for c in graph[x]:
        color[c] = color[x]

for i in range(q):
    if s[i][0] == 1:
        change(s[i][1])
        print(color[s[i][1]])
    else:
        print(color[s[i][1]])
        color[s[i][1]] = s[i][2]
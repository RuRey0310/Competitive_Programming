n = int(input())
x = [list(map(int, list(input().split()))) for i in range(n)]

x.sort(key=lambda x: x[2])

for cx in range(101):
    for cy in range(101):
        height = abs(x[n - 1][0] - cx) + abs(x[n - 1][1] - cy) + x[n - 1][2]
        for i in range(n):
            sub = max(height - abs(x[i][0] - cx) - abs(x[i][1] - cy), 0)
            if sub != x[i][2]:
                break
            if i == n - 1:
                print(cx, cy, height)
                exit()

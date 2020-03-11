import copy
a = [list(input()) for i in range(10)]

def dfs(x, y):
    if x >= 10 or y >= 10 or x < 0 or y < 0 or boo[x][y] == "x":
        return

    boo[x][y] = "x"

    dfs(x, y + 1)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x - 1, y)

for i in range(10):
    for j in range(10):
        if a[i][j] == "x":
            boo = copy.deepcopy(a)
            boo[i][j] = "o"
            cnt = 0
            for k in range(10):
                for l in range(10):
                    if boo[k][l] == "o":
                        dfs(k, l)
                        cnt += 1
            if cnt == 1:
                print("YES")
                exit()

print("NO")

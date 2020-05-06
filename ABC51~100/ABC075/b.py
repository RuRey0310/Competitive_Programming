h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

a = [0, 0, 1, -1, 1, -1, 1, -1]
b = [1, -1, 1, -1, -1, 1, 0, 0]
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            sub = 0
            for k in range(8):
                if i + a[k] >= 0 and j + b[k] >= 0 and i + a[k] < h and j + b[k] < w:
                    if s[i + a[k]][j + b[k]] == '#':
                        sub += 1
            s[i][j] = sub

for i in range(h):
    for j in range(w):
        print(s[i][j], end="")
    print()
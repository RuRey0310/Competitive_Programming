h, w = map(int, input().split())
a = [list(input()) for i in range(h)]

for i in range(-1, h + 1):
    for j in range(-1, w + 1):
        if i == -1 or j == -1 or i == h or j == w:
            print("#",end = "")
        else:
            print(a[i][j], end="")
    print()

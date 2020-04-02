h, w = map(int, input().split())
s = [list(input()) for i in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            if s[min(i + 1, h - 1)][j] != "#" and s[i][min(j + 1, w - 1)] != "#" and s[i - 1][j] != "#" and s[i][j - 1] != "#":
                print("No")

                exit()

print("Yes")
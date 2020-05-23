n = int(input())
a = [list(input()) for i in range(n)]

#-97
mozi = [[False] * 26 for i in range(n)]
for i in range(n):
    for j in range(n):
        mozi[i][ord(a[i][j]) - 97] = True

sub = ""
for i in range(n):
    for j in range(26):
        if mozi[i][j] and mozi[n - i - 1][j]:
            sub += chr(97 + j)
            break
        if j == 25:
            print("-1")
            exit()

print(sub)
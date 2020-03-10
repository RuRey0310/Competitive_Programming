a = [list(map(int, list(input().split()))) for i in range(3)]
n = int(input())
b = [int(input()) for i in range(n)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if a[j][k] == b[i]:
                a[j][k] = True

for i in range(3):
    cnt = 0
    for j in range(3):
        if a[i][j] == True:
            cnt += 1
        if cnt == 3:
            print("Yes")
            exit()

for i in range(3):
    cnt = 0
    for j in range(3):
        if a[j][i] == True:
            cnt += 1
        if cnt == 3:
            print("Yes")
            exit()

if a[0][0] == True and a[1][1] == True and a[2][2] == True:
    print("Yes")
    exit()

if a[2][0] == True and a[1][1] == True and a[0][2] == True:
    print("Yes")
    exit()

print("No")

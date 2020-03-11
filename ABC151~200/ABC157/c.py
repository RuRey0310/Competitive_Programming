n, m = map(int, input().split())
sc = [list(map(int, list(input().split()))) for i in range(m)]

sc.sort()

hantei = [-1] * n
for i in range(m):
    if hantei[sc[i][0] - 1] == -1 or hantei[sc[i][0] - 1] == sc[i][1]:
        hantei[sc[i][0] - 1] = sc[i][1]
    else:
        print("-1")
        exit()

leng = len(hantei)
for i in range(leng):
    if i == 0 and hantei[i] == 0 and leng != 1:
        print("-1")
        exit()
    else:
        if hantei[i] != -1:
            print(hantei[i], end="")
        else:
            if i != 0:
                print("0", end="")
            elif leng == 1:
                print("0")
            else:
                print("1", end="")
              

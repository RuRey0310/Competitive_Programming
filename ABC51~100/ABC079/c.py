a = list(input())

for i in range(2 ** 3):
    switch = [0] * 3
    for j in range(3):
        if ((i >> j) & 1):
            switch[j] = 1

    sum = int(a[0])
    for k in range(3):
        if switch[k] == 0:
            sum -= int(a[k + 1])
        else:
            sum += int(a[k + 1])
    if sum == 7:
        for k in range(3):
            print(a[k], end="")
            if switch[k] == 1:
                print("+", end="")
            else:
                print("-", end="")
        print(a[3], end="")
        print("=7")
        break 

k = [list(map(int, list(input().split()))) for i in range(3)]

for a1 in range(101):
    for a2 in range(101):
        for a3 in range(101):
            if (k[0][0] - a1) == (k[0][1] - a2) == (k[0][2] - a3):
                if (k[1][0] - a1) == (k[1][1] - a2) == (k[1][2] - a3):
                    if (k[2][0] - a1) == (k[2][1] - a2) == (k[2][2] - a3):
                        if k[0][0] - a1 >= 0 and k[0][1] - a2 >= 0 and k[0][2] - a3 >= 0:
                            if (k[1][0] - a1) >= 0 and (k[1][1] - a2) >= 0 and (k[1][2] - a3) >= 0:
                                if (k[2][0] - a1) >= 0 and (k[2][1] - a2) >= 0 and (k[2][2] - a3) >= 0:
                                    print("Yes")
                                    exit()

print("No")
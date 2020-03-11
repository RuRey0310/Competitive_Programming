n, m, x, y = map(int, input().split())
xn = list(map(int, input().split()))
ym = list(map(int, input().split()))

for z in range(-100, 101):
    war = False
    if x < z and z <= y:
        for i in range(n):
            for j in range(m):
                if xn[i] >= z or ym[j] < z:
                    war = True
        if war == False:
            print("No War")
            exit()
print("War")

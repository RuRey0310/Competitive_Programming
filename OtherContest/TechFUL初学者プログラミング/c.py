n = int(input())
dm = [list(map(int, list(input().split()))) for i in range(n)]

cash = 0
for i in range(n):
    if dm[i][0] == 0:
        cash += dm[i][1]
    else:
        if dm[i][1] > cash:
            cash = 0
        else:
            cash -= dm[i][1]
        
print(cash)
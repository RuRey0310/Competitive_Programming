n, t = map(int, input().split())
ct = [list(map(int, list(input().split()))) for i in range(n)]

ct.sort(key=lambda x: x[0])

for i in range(n):
    if ct[i][1] <= t:
        print(ct[i][0])
        exit()
    if i == n - 1:
        print("TLE")

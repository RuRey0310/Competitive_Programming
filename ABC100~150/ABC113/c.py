n, m = map(int, input().split())
Pre = [list(map(int, list(input().split()))) for i in range(m)]

for i in range(1, m + 1):
    Pre[i - 1].append(i)

Pre.sort()

cnt = 1
Pre[0][1] = cnt
for i in range(1,m):
    if Pre[i - 1][0] != Pre[i][0]:
        cnt = 1
        Pre[i][1] = cnt
    else:
        cnt += 1
        Pre[i][1] = cnt

Pre.sort(key=lambda x: x[2])

for i in range(m):
    print("{0:06d}{1:06d}".format(Pre[i][0],Pre[i][1]))

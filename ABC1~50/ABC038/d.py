n = int(input())
wh = [list(map(int, list(input().split()))) for i in range(n)]

wh.sort(key=lambda x: x[1], reverse=True)
wh.sort(reverse=True)

ans = 1
pre = 1
mh = wh[0][0]
mw = wh[0][1]
for i in range(1,n):
    if wh[i][0] < mh and wh[i][1] < mw:
        pre += 1
        mh = wh[i][0]
        mw = wh[i][1]
    else:
        ans = max(ans, pre)

print(max(ans, pre))
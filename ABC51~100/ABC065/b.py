import sys
sys.setrecursionlimit(200000)
n = int(input())
a = [int(input()) for i in range(n)]

switch = [False] * (n + 1)
def button(x,cnt):
    if switch[x]:
        print(-1)
        return -1
    if x == 2:
        print(cnt)
        return
    switch[x] = True
    button(a[x - 1], cnt + 1)
    return cnt

ans = button(1, 0)
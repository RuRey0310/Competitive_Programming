n, k = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(n)]

sub = 0
ab.sort()
for i in range(n):
    sub += ab[i][1]
    if sub >= k:
        print(ab[i][0])
        break

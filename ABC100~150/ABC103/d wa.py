n, m = map(int, input().split())
ab = [list(map(int, list(input().split()))) for i in range(m)]

ab.sort(key=lambda x: x[1])
sub = -1
ans = 0
for i in range(m):
    if ab[i][0] <= sub and ab[i][1] > sub:
        continue
    else:
        ans += 1
        sub = ab[i][1] - 1

print(ans)
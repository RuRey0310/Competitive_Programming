s = list(input())
n = int(input())
lr = [list(map(int, list(input().split()))) for i in range(n)]

lr.sort(key=lambda x: x[1], reverse=True)
lr.sort(key=lambda x: x[0])

dp = [-1] * len(s)
cnt = 0
dd = []
i = 1
while i < len(lr):
    if lr[i][1] <= lr[i - 1][1]:
        del lr[i]
        continue
    elif lr[i][0] <= lr[i - 1][1] and lr[i][1] > lr[i - 1][1]:
        lr[i - 1][1] = lr[i][1]
        del lr[i]
        continue
    i += 1
       

sub = []
ans = []
st = -1
go = -1
for i in range(len(lr)):
    d = s[lr[i][0] - 1 : lr[i][1]]
    d.sort()
    s[lr[i][0] - 1 : lr[i][1]] = d

ans = ''.join(s)
print(ans)
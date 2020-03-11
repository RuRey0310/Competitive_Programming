import collections
n = int(input())
v = list(map(int, input().split()))

x = []
y = []
for i in range(n):
    if (i + 1) % 2 == 1:
        x.append(v[i])
    else:
        y.append(v[i])

xcnt = collections.Counter(x)
ycnt = collections.Counter(y)

x_max = []
if len(xcnt) > 1:
    x_max.append(xcnt.most_common()[0])
    x_max.append(xcnt.most_common()[1])
else:
    x_max.append(xcnt.most_common()[0])
    x_max.append(xcnt.most_common()[0])

y_max = []
if len(ycnt) > 1:
    y_max.append(ycnt.most_common()[0])
    y_max.append(ycnt.most_common()[1])
else:
    y_max.append(ycnt.most_common()[0])
    y_max.append(ycnt.most_common()[0])

ans = float("inf")
for i in range(2):
    for j in range(2):
        if x_max[i][0] != y_max[j][0]:
            sub = n - x_max[i][1] - y_max[j][1]
            ans = min(ans, sub)
if ans == float("inf"):
    ans = n // 2
print(ans)

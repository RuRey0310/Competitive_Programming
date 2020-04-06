n = int(input())
a = list(map(int, input().split()))

aa = [0]
a = aa + a
a.append(0)

sub = 0
for i in range(n + 1):
    sub += abs(a[i + 1] - a[i])

for i in range(1, n + 1):
    print(sub - (abs(a[i] - a[i - 1]) + abs(a[i] - a[i + 1])) + abs(a[i + 1] - a[i - 1]))

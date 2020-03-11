n = int(input())
t = [int(input()) for i in range(n)]

ans = float("inf")
for i in range(2 ** n):
    zero = 0
    one = 0
    switch = [0] * n
    for j in range(n):
        if((i >> j) & 1):
            switch[j] = 1
    for k in range(n):
        if switch[k] == 0:
            zero += t[k]
        else:
            one += t[k]
    ans = min(ans, max(zero, one))

print(ans)

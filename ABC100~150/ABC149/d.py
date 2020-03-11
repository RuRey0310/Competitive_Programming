n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())

def func(i):
    if i == 'r':
        return 'p'
    elif i == 's':
        return 'r'
    else:
        return 's'

tp = [0] * n
for i in range(k):
    tp[i] = func(t[i])
for i in range(k, n):
    if tp[i - k] == func(t[i]):
        tp[i] = '-'
    else:
        tp[i] = func(t[i])
ans = (tp.count('r') * r) + (tp.count('p') * p) + (tp.count('s') * s)

print(ans)

n = int(input())
t, a = map(int, input().split())
h = list(map(int,input().split()))

mintemp = 10 ** 9
ans = 0
for i in range(n):
    temp = t - (h[i] * 0.006)
    if mintemp > abs(a - temp):
        mintemp = abs(a - temp)
        ans = i
print(ans + 1)

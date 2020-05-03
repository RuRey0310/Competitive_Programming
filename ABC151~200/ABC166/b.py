n, k = map(int, input().split())

d = [0] * k
a = []
snuk = [False] * n
for i in range(k):
    d[i] = int(input())
    a = list(map(int, input().split()))
    for j in a:
        snuk[j - 1] = True
    

ans = 0
for i in range(n):
    if snuk[i] == False:
        ans += 1


print(ans)
n = int(input())
p = list(map(int,input().split()))

ans = n
mins = 10 ** 9
for i in range(n):
    mins = min(mins, p[i])
    if mins < p[i]:
        ans -= 1

print(ans)

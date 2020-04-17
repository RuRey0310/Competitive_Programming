n = int(input())
k = int(input())

ans = 1
for i in range(n):
    sub = ans  * 2
    sub2 = ans + k
    if sub > sub2:
        ans += k
    else:
        ans *= 2

print(ans)
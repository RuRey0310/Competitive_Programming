n = list(input())
ans = 0
sub = -1
for i in range(len(n)):
    if sub == n[i]:
        ans += 1
    else:
        sub = n[i]
        ans = 1
    if ans >= 3:
        break

if ans >= 3:
    print("Yes")
else:
    print("No")
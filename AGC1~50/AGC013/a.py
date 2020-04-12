n = int(input())
a = list(map(int, input().split()))

ans = 0
if a[0] < a[1]:
    plus = True
else:
    plus = False
for i in range(n - 1):
    if a[i] == a[i + 1] + 1:
        if plus == False:
            ans += 1
        else:
            plus = True
    elif a[i] == a[i + 1] - 1:
        if plus == True:
            ans += 1
        else:
            plus = False

print(ans)
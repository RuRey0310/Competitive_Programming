n = int(input())
a = list(map(int, input().split()))

flag = 1
for i in range(n):
    if a[i] % 2 == 0:
        if a[i] % 3 != 0 and a[i] % 5 != 0:
            flag = 0

if flag == 0:
    print("DENIED")
else:
    print("APPROVED")

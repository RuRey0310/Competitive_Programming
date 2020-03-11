n = int(input())
a = [0] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
asort = sorted(a, key=lambda x: x[1])

sum = 0
for i in range(n):
    sum += asort[i][0]
    if sum > asort[i][1]:
        print("No")
        exit()
print("Yes")

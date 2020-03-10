n = int(input())
l = list(map(int, input().split()))

x = 0
maxside = 0
for i in range(n):
    if maxside < l[i]:
        maxside = l[i]
        x = i
del l[x]
sum = 0
for i in range(n - 1):
    sum += l[i]

if sum > maxside:
    print("Yes")
else:
    print("No")

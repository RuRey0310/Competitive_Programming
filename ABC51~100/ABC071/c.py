n = int(input())
a = list(map(int, input().split()))

a.sort(reverse = True)

width = 0
height = 0
cnt = 0
for i in range(n - 1):
    if a[i] == a[i + 1] and cnt == 0:
        width = a[i]
        cnt += 1
        del a[i + 1]
    elif a[i] == a[i + 1] and cnt == 1:
        height = a[i]
        break

print(width * height)
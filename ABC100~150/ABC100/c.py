n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
even = []
for i in range(n):
    if a[i] % 2 == 0:
        even.append(a[i])

three = 0
for i in range(len(even)):
    sub = even[i]
    while sub % 2 == 0:
        three += 1
        sub = sub / 2

print(three)
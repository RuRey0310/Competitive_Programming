n = int(input())
a = list(map(int,input().split()))

if n % 2 == 0:
    for i in reversed(range(n)):
        if i % 2 == 1:
            print(a[i], end=" ")
    for i in range(n):
        if i % 2 == 0:
            print(a[i], end=" ")
else:
    for i in reversed(range(n)):
        if i % 2 == 0:
            print(a[i], end=" ")
    for i in range(n):
        if i % 2 == 1:
            print(a[i], end=" ")
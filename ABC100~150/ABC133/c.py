l, r = map(int, input().split())

a = 2018

for i in range(l, r):

    for j in range(i + 1, r + 1):
        a = min(a, (i * j) % 2019)
        if a == 0:
            print(a)
            exit()

print(a)

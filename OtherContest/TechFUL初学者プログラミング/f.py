x, m, r = map(int, input().split())

for i in range(1, 10**5):
    sub = x * i
    if sub % m == r:
        print("Yes")
        exit()

print("No")
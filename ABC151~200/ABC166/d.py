x = int(input())

for a in range(1,1001):
    sub = a ** 5
    ss = sub - x
    for b in range(-1000, 1000):
        if b ** 5 == ss:
            print(a, b)
            exit()
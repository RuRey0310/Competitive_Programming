x = int(input())

def Prime(n):
    for p in range(2, n):
        if n % p == 0:
            return 0
    return 1

for i in range(x, 10 ** 8):
    sosu = Prime(i)
    if sosu == 1:
        print(i)
        break

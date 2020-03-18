n = int(input())

n = abs(n)
a = 0
i = 0
if n == 0:
    print("0")
    exit()
if n % 2 == 0:
    while True:
        i += 1
        a += i
        if a % 2 == 0 and a >= n:
            break
else:
    while True:
        i += 1
        a += i
        if a % 2 == 1 and a >= n:
            break

print(i)
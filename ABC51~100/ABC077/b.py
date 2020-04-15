n = int(input())

for i in range(10 ** 5):
    if n == (i * i):
        print(i * i)
        exit()
    if n <= (i * i):
        break


print((i - 1) * (i - 1))
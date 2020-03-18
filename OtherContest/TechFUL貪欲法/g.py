n = int(input())

n = abs(n)
a = 0
i = 0
while a < n:
    i += 1
    a += i

if a == n:
    print(i)
    exit()

a -= i
ab = n - a
ab *= 2
print((i - 1) + ab)
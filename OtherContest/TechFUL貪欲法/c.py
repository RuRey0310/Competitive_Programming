import math
x = float(input())

a = math.ceil(x)
b = math.floor(x)

aa = abs(a - x)
bb = abs(b - x)

if aa > bb:
    if b % 2 == 1:
        print(b + 1)
    else:
        print(b)
else:
    if a % 2 == 1:
        print(a + 1)
    else:
        print(a)

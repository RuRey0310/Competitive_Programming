a, b, c, d = map(int, input().split())

while a > 0:
    c -= b
    if c <= 0:
        print("Yes")
        exit()
    a -= d

print("No")
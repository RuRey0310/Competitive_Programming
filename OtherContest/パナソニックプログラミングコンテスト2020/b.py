h, w = map(int, input().split())

a = h * w

if h == 1 or w == 1:
    print("1")
else:
    if a % 2 == 0:
        print(a // 2)
    else:
        print((a // 2) + 1)
        
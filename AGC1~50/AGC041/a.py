n, a, b = map(int, input().split())


if (b - a) % 2 == 0:
    print((b - a) // 2)
else:
    test = (b - a) // 2
    left = a - 1
    right = n - b
    if left >= right:
        print(n - a - test)
    else:
        print(b - 1 - test)

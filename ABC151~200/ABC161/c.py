n, k = map(int, input().split())

if n % k == 0:
    print("0")
else:
    sub = n % k
    sub2 = n // k
    sub3 = (k * (sub2 + 1)) - n
    print(min(sub, sub3))
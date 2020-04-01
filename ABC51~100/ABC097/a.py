a, b, c, d = map(int, input().split())

if abs(a - c) <= d:
    print("Yes")
elif abs(b - a) <= d and abs(c - b) <= d:
    print("Yes")
else:
    print("No")
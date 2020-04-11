a, b = map(int, input().split())

ab = str(a) + str(b)
ab = int(ab)
for i in range(1, 100000):
    if i * i == ab:
        print("Yes")
        exit()

print("No")
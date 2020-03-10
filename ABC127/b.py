r, d, x0 = map(int, input().split())

x = [0] * 11
x[0] = x0

for i in range(1, 11):
    x[i] = r * x[i - 1] - d

for i in range(1, 11):
    print(x[i])

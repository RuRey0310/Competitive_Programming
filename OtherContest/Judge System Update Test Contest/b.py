n = int(input())
red = []
blue = []
for i in range(n):
    x, c = map(str, input().split())
    if c == "R":
        red.append(int(x))
    else:
        blue.append(int(x))

red.sort()
blue.sort()
for i in red:
    print(i)
for i in blue:
    print(i)
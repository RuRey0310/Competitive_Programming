c = list(input())
d = list(input())

for i in range(3):
    if c[2 - i] != d[i]:
        print("NO")
        exit()

print("YES")
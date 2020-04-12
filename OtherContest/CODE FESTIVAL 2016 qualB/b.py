n, a, b = map(int, input().split())
s = list(input())

total = 0
bcnt = 0
for i in range(n):
    if s[i] == "c":
        print("No")
    elif s[i] == "a":
        if total < a + b:
            total += 1
            print("Yes")
        else:
            print("No")
    elif s[i] == "b":
        if total < a + b and bcnt < b:
            total += 1
            bcnt += 1
            print("Yes")
        else:
            print("No")

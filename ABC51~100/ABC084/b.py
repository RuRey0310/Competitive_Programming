a, b = map(int, input().split())
s = list(input())
if len(s) != a + b + 1:
    print("No")
elif s[a] != "-":
    print("No")
else:
    for i in range(a):
        if not s[i].isdecimal():
            print("No")
            exit()
    for i in range(a + 1, len(s)):
        if not s[i].isdecimal():
            print("No")
            exit()
    print("Yes")
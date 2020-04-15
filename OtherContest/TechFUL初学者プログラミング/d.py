s = list(input())

if s[0] != "2" or s[-1] != "0":
    print("No")
    exit()
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] != "2":
            print("No")
            exit()
    else:
        if s[i] != "0":
            print("No")
            exit()
print("Yes")
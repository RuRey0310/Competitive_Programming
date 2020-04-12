n = int(input())

s = str(n)
s = list(s)
for i in range(len(s)):
    if s[i] == "7":
        print("Yes")
        exit()

print("No")
s = list(input())
t = list(input())

lang = len(s) - 1

for i in range(len(s)):
    sub = s[lang]
    del s[lang]
    s.insert(0, sub)
    if s == t:
        print("Yes")
        exit()

print("No")

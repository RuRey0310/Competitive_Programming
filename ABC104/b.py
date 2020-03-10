s = list(input())

a = False
c = False
small = False
for i in range(len(s)):
    if i == 0 and s[i] == "A":
        a = True
    elif a == True and i >= 2 and i < len(s) - 1 and s[i] == "C" and c == False:
        c = True
    elif s[i] >= "a" and s[i] <= "z":
        small = True
    else:
        small = False
        break

if a == True and c == True and small == True:
    print("AC")
else:
    print("WA")

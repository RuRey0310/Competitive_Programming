s = list(input())
t = list(input())

r1 = [-1] * 26
r2 = [-1] * 26

for i in range(len(s)):
    ss = ord(s[i]) - 97
    tt = ord(t[i]) - 97
    if r1[ss] >= 0:
        if r1[ss] != tt:
            print("No")
            exit()
    if r2[tt] >= 0:
        if r2[tt] != ss:
            print("No")
            exit()
    if r1[ss] < 0:
        r1[ss] = tt
    if r2[tt] < 0:
        r2[tt] = ss

print("Yes")

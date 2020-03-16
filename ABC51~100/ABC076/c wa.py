s = list(input())
t = list(input())

lengs = len(s)
lengt = len(t)

que = 0
j = 0
minus = 0
if lengs > lengt:
    for i in range(lengs):
        if s[i] == "?":
            que += 1
        elif s[i] == t[j]:
            j += 1
            minus += 1
        elif s[i] != t[j]:
            que = 0
            j = 0
            minus = 0
        if lengt - minus == que:
            break
        if i == (lengs - 1):
            print("UNRESTORABLE")
            exit()
    k = 0
    while k < lengs:
        if k == (i - lengt + 1):
            for z in range(lengt):
                print(t[z], end="")
            k += lengt
        else:
            if s[k] == "?":
                print("a", end="")
            else:
                print(s[k], end="")
        k += 1            
else:
    print("UNRESTORABLE")
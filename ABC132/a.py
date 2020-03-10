s = input()
slist = list(s)

slist.sort()

if (slist[0] == slist[1] and slist[1] != slist[2] and slist[2] == slist[3]):
    print("Yes")
else:
    print("No")

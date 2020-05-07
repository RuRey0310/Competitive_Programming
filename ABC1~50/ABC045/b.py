sa = list(input())
sb = list(input())
sc = list(input())

next = sa[0]
del sa[0]
while len(sa) >= 0 and len(sb) >= 0 and len(sc) >= 0:
    if next == "a":
        if len(sa) == 0:
            print("A")
            break
        next = sa[0]
        del sa[0]
    elif next == "b":
        if len(sb) == 0:
            print("B")
            break
        next = sb[0]
        del sb[0]
    elif next == "c":
        if len(sc) == 0:
            print("C")
            break
        next = sc[0]
        del sc[0]
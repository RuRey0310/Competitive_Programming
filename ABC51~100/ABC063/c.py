n = int(input())
s = [int(input()) for i in range(n)]

ans = 0
sub = sum(s)
if sub % 10 != 0:
    print(sub)
else:
    l = []
    for i in range(n):
        if s[i] % 10 != 0:
            l.append(s[i])
    l.sort()
    for j in l:
        sub -= j
        if sub % 10 != 0:
            break
    
    if sub % 10 == 0:
        print("0")
    else:
        print(sub)
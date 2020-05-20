s, t = map(int, input().split())

if s == 0 and t == 23:
    for i in range(0, 24):
        print(i, end=" ")
elif s == t:
    for i in range(0, 24):
        print(i, end=" ")
else:
    for i in range(0, 24):
        if (i < s):
            print(i, end=" ")
        elif (i >= t):
            print(i, end=" ")
            
        
s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)
ss = ''.join(s)
tt = ''.join(t)

if ss < tt:
    print("Yes")
else:
    print("No")
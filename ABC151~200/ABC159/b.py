import math
s = list(input())
n = len(s)

for i in range(n):
    if s[i] != s[n - i - 1]:
        print("No")
        exit()
        
aa = math.floor((n - 1) / 2)
bb = math.ceil((n + 3) / 2)
a = s[0:aa]
b = s[bb - 1:n]

alen = len(a)
blen = len(b)

for i in range(alen):
    if a[i] != a[alen - i - 1]:
        print("No")
        exit()

for i in range(blen):
    if b[i] != b[blen - i - 1]:
        print("No")
        exit()

print("Yes")
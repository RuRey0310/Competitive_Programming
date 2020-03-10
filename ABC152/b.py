a,b = map(int, input().split())

s = ""
z = ""

for i in range(b):
    s += str(a)
for j in range(a):
    z += str(b)
if s > z:
    print(z)
else:
    print(s)

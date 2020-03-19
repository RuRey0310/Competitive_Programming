n = list(input())

mod = 0
for i in range(len(n)):
    mod += int(n[i])

n = ''.join(n)
nint = int(n)
if nint % mod == 0:
    print("Yes")
else:
    print("No")
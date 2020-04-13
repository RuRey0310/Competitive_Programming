n = list(input())

keta = 0
sub = ""
for i in range(len(n)):
    sub += n[i]
    keta += int(n[i])

sub = int(sub)
if sub % keta == 0:
    print("Yes")
else:
    print("No")
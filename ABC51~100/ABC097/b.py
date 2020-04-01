x = int(input())

sub = []
for i in range(1, 100):
    for j in range(2, 100):
        sub.append(i ** j)

sub.sort()
for i in range(len(sub)):
    if sub[i] > x:
        ans = sub[i - 1]
        break

print(ans)
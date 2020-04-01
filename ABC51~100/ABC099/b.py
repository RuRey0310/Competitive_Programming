a, b = map(int, input().split())

sub = 0
for i in range(1, b - a + 1):
    sub += i

print(sub - b)
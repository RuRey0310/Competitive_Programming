n = int(input())
a = int(input())

ans = 0
sub = n
while sub <= a:
    sub *= n

print(sub - a)